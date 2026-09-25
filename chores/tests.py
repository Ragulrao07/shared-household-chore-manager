import json
from django.test import TestCase, Client
from django.utils import timezone
from .models import Chore

class ChoreModelTest(TestCase):
    def setUp(self):
        self.chore = Chore.objects.create(
            name="Wash Dishes",
            description="Clean all dirty dishes in the sink",
            frequency="DAILY",
            due_date=timezone.now()
        )

    def test_chore_creation(self):
        """Test that a chore is created with the correct data."""
        self.assertEqual(self.chore.name, "Wash Dishes")
        self.assertEqual(self.chore.frequency, "DAILY")
        self.assertFalse(self.chore.is_deleted)

    def test_chore_string_representation(self):
        """Test the __str__ method of the Chore model."""
        self.assertEqual(str(self.chore), "Wash Dishes")

    def test_chore_soft_delete(self):
        """Test that the custom delete method performs a soft delete."""
        self.chore.delete()
        self.assertTrue(self.chore.is_deleted)


class ChoreApiIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chore_create_and_fetch_lifecycle(self):
        """Test creating a chore via POST and fetching it via GET."""
        payload = {
            'title': 'Vacuum the living room'
        }

        # 1. Create a chore via POST /api/chores/
        post_response = self.client.post(
            '/api/chores/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(post_response.status_code, 201)
        post_data = post_response.json()
        self.assertEqual(post_data['title'], 'Vacuum the living room')
        self.assertFalse(post_data['is_completed'])
        self.assertIn('id', post_data)

        # 2. Fetch chores via GET /api/chores/
        get_response = self.client.get('/api/chores/')
        self.assertEqual(get_response.status_code, 200)
        get_data = get_response.json()

        # 3. Confirm newly created chore is present in response
        matching_chores = [c for c in get_data if c['id'] == post_data['id']]
        self.assertEqual(len(matching_chores), 1)
        self.assertEqual(matching_chores[0]['title'], 'Vacuum the living room')
        self.assertFalse(matching_chores[0]['is_completed'])
