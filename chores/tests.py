from django.test import TestCase

# Create your tests here.
from django.test import TestCase
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
