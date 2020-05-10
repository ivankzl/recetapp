from django.db import models
from tinymce.models import HTMLField
from django.contrib.postgres.fields import JSONField
from slugify import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    cover_picture = models.ImageField(upload_to='photos')
    ingredients = JSONField()
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField('slug', max_length=60, blank=True)
    categories = models.ManyToManyField(Category)

    #Then override models save method:
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title) 
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
