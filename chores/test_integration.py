from django.test import TestCase, Client
import json
from chores.models import Chore

class ChoreIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_full_chore_lifecycle(self):
        # 1. Create a chore via API
        payload = {"name": "Wash Dishes", "frequency": "daily", "description": "Kitchen sink cleanout"}
        create_res = self.client.post(
            "/api/chores/",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(create_res.status_code, 201)
        chore_id = create_res.json()["id"]

        # 2. Verify chore exists in DB
        chore = Chore.objects.get(id=chore_id)
        self.assertEqual(chore.name, "Wash Dishes")
        self.assertFalse(chore.is_completed)

        # 3. Toggle completion
        toggle_res = self.client.post(f"/api/chores/{chore_id}/toggle/")
        self.assertEqual(toggle_res.status_code, 200)
        self.assertTrue(toggle_res.json()["is_completed"])

        # 4. Verify Prometheus metrics endpoint is healthy
        metrics_res = self.client.get("/metrics")
        self.assertEqual(metrics_res.status_code, 200)
        self.assertIn(b"chores_created_total", metrics_res.content)
