from django.db import models
from django.conf import settings

class Chore(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='daily')
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_chores'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        """Perform soft delete by marking is_deleted as True."""
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.name