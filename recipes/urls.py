from django.conf.urls import include, url
from .views import (index, RecipeListView, RecipeDetailView, AboutView)

from . import views

app_name = 'recipes'

urlpatterns = [
    url(r'^$',
        RecipeListView.as_view(),
        name='index'),
    
    url(r'^recetas/(?P<slug>[-\w]+)/$',
        RecipeDetailView.as_view(),
        name='recipe-detail'),

    url(r'^about/$',
        AboutView.as_view(),
        name='about'),
]
