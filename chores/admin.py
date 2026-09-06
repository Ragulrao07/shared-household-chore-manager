from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Chore

@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency', 'due_date', 'is_deleted')
    list_filter = ('frequency', 'is_deleted')
    search_fields = ('name', 'description')
