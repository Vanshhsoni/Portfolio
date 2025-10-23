# In core/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Project  # <-- Import your models

def home(request):
    categories = Category.objects.prefetch_related('projects').all()
    featured_project = Project.objects.order_by('-date_completed').first()
    context = {
        'all_categories': categories,
        'featured': featured_project,
    }
    return render(request, 'home.html', context)

def project_detail(request, slug):
    # Get the project with the matching slug. If not found, return a 404 page.
    project = get_object_or_404(Project, slug=slug)
    
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def about(request):
    """
    A simple, static view for the About Me page.
    """
    return render(request, 'about.html')