# In core/urls.py (Create this new file)

from django.urls import path
from . import views  # <-- Imports views from the current 'core' app

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<slug:slug>/', views.project_detail, name='project-detail'),
    path('about/', views.about, name='about'),
]