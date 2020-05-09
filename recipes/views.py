from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Recipe

def index(request):
  return render(request, 'recipes/index.html')

def recipes(request):
  recipe_list = Recipe.objects.order_by('-created_at')
  page = request.GET.get('page', 1)

  paginator = Paginator(recipe_list, 2)

  try:
    recipes = paginator.page(page)
  except PageNotAnInteger:
      recipes = paginator.page(1)
  except EmptyPage:
      recipes = paginator.page(paginator.num_pages)

  context = {
    'recipes': recipes,
  }
  return render(request, 'recipes/recipes.html', context)
