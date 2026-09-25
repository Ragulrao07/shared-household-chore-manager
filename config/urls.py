from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.generic import TemplateView
from chores.views import chore_list_api

urlpatterns = [
    # Serve React frontend index.html at root
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # Silence favicon 404s
    path('favicon.ico', lambda request: HttpResponse(status=204)),
    
    # Admin interface
    path('admin/', admin.site.urls),

    # Chores API
    path('api/chores/', chore_list_api, name='chore_list_api'),
]
