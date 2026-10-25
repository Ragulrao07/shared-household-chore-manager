from django.contrib import admin
from .models import Chore

@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency', 'is_completed', 'created_at')
    list_filter = ('frequency', 'is_completed')
    search_fields = ('name', 'description')
