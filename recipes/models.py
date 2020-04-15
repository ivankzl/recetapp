from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    created_at = models.DateTimeField('date published')