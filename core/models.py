# In core/models.py

from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# ==================================
#  1. CATEGORY MODEL
# ==================================
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        # Fixes the plural name in the Django admin
        verbose_name_plural = "Categories" 

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically create the slug from the name if it's empty
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# ==================================
#  2. PROJECT MODEL
# ==================================
class Project(models.Model):
    # --- Main Relationship ---
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.SET_NULL, null=True)
    
    # --- For the Landing Page Card ---
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    short_description = models.CharField(max_length=250, help_text="The short summary shown on the portfolio grid.")
    
    # --- For the Detail Page ---
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    technologies_used = models.CharField(max_length=200, blank=True, help_text="e.g., HTML, CSS, Django, Photoshop")
    detailed_description = models.TextField(blank=True, help_text="The full case study/review for the project detail page.")
    project_link = models.URLField(max_length=200, blank=True, help_text="The URL to the live site or GitHub repo.")
    main_image = models.ImageField(upload_to='projects/main_images/', blank=True, null=True, help_text="A large banner image for the detail page.")

    class Meta:
        # Order projects by date, newest first
        ordering = ['-date_completed']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Automatically create the slug from the title if it's empty
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        # This helps create links to the detail page automatically
        return reverse('project-detail', kwargs={'slug': self.slug})
    
    def technology_list(self):
        """
        Splits the 'technologies_used' string by comma 
        and returns a list of cleaned-up strings.
        """
        if not self.technologies_used:
            return []
        return [tech.strip() for tech in self.technologies_used.split(',') if tech.strip()]