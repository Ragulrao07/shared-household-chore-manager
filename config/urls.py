from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.generic.base import RedirectView

urlpatterns = [
    # Automatically forward root to the admin dashboard
    path('', RedirectView.as_view(url='admin/', permanent=False)),
    
    # Silence favicon 404s
    path('favicon.ico', lambda request: HttpResponse(status=204)),
    
    # Admin interface
    path('admin/', admin.site.urls),
]