from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.generic import TemplateView
from chores.views import chore_list_api, metrics_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('favicon.ico', lambda request: HttpResponse(status=204)),
    path('admin/', admin.site.urls),
    path('api/chores/', chore_list_api, name='chore_list_api'),
    path('metrics', metrics_view, name='metrics'),
]
