from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from braces.views import StaticContextMixin

from .models import Recipe

def index(request):
  return render(request, 'recipes/index.html')

class RecipeListView(StaticContextMixin, ListView): 
  template_name = 'recipes/recipes.html'
  context_object_name = 'recipes'
  static_context = {'title': ('Recetas')}

  def get_queryset(self):
    queryset = Recipe.objects.order_by('-created_at')

    return queryset


class RecipeDetailView(StaticContextMixin, DetailView):

    context_object_name = 'recipe'
    template_name = 'recipes/detail_recipe.html'
    model = Recipe
    static_context = {'title': ('Receta - Detalle')}
