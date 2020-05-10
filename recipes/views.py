from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from braces.views import StaticContextMixin
import pdb

from .models import Recipe, Category

def index(request):
  return render(request, 'recipes/index.html')

class RecipeListView(StaticContextMixin, ListView): 
  template_name = 'recipes/recipes.html'
  context_object_name = 'recipes'
  static_context = {'title': 'Recetas', 'categories': Category.objects.all()}

  def get_queryset(self):
    queryset = Recipe.objects.order_by('-created_at')
    category_filter_id=self.request.GET.get('categoria')
    if category_filter_id:
      queryset = queryset.filter(categories__id=category_filter_id)

    return queryset


class RecipeDetailView(StaticContextMixin, DetailView):

    context_object_name = 'recipe'
    template_name = 'recipes/detail_recipe.html'
    model = Recipe
    static_context = {'title': 'Receta - Detalle', 'categories': Category.objects.all()}


class AboutView(StaticContextMixin, TemplateView):
    
    template_name = 'recipes/about.html'
    static_context = {'title': 'Acerca de'}
