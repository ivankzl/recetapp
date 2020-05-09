from django.db import models
from tinymce.models import HTMLField
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    cover_picture = models.ImageField(upload_to='photos')
    ingredients = JSONField()
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
