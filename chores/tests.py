import json
from django.test import TestCase, Client
from .models import Chore

class ChoreModelTest(TestCase):
    def setUp(self):
        self.chore = Chore.objects.create(
            name="Sweep floors",
            frequency="daily"
        )

    def test_chore_creation(self):
        self.assertEqual(self.chore.name, "Sweep floors")
        self.assertEqual(self.chore.frequency, "daily")
        self.assertFalse(self.chore.is_completed)

    def test_chore_soft_delete(self):
        self.chore.delete()
        self.assertTrue(self.chore.is_deleted)


class ChoreApiIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chore_create_and_fetch_lifecycle(self):
        payload = {
            'name': 'Vacuum the living room',
            'frequency': 'daily'
        }

        # 1. POST /api/chores/
        post_response = self.client.post(
            '/api/chores/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(post_response.status_code, 201)
        post_data = post_response.json()
        self.assertEqual(post_data['name'], 'Vacuum the living room')
        self.assertFalse(post_data['is_completed'])
        self.assertIn('id', post_data)

        # 2. GET /api/chores/
        get_response = self.client.get('/api/chores/')
        self.assertEqual(get_response.status_code, 200)
        get_data = get_response.json()

        # 3. Confirm chore is returned
        matching = [c for c in get_data if c['id'] == post_data['id']]
        self.assertEqual(len(matching), 1)
        self.assertEqual(matching[0]['name'], 'Vacuum the living room')
