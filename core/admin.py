# In core/admin.py

from django.contrib import admin
from .models import Category, Project

# --- Basic Registration ---
# admin.site.register(Category)
# admin.site.register(Project)

# --- A Better, More Organized Admin ---
# This will make it look much cleaner

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Auto-fills slug from name

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_completed')
    list_filter = ('category', 'date_completed')
    search_fields = ('title', 'short_description', 'technologies_used')
    prepopulated_fields = {'slug': ('title',)} # Auto-fills slug from title
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'date_completed')
        }),
        ('Landing Page Content', {
            'fields': ('thumbnail', 'short_description')
        }),
        ('Detail Page Content', {
            'fields': ('main_image', 'detailed_description', 'technologies_used', 'project_link')
        }),
    )