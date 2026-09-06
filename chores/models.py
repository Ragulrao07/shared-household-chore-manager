from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Chore(models.Model):
    FREQUENCY_CHOICES = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='WEEKLY')
    due_date = models.DateTimeField()
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='assigned_chores')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, **kwargs):
        """Soft delete implementation"""
        self.is_deleted = True
        self.save()
