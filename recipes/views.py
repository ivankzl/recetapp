from django.shortcuts import render

from .models import Recipe

def index(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    return render(request, 'recipes/index.html', context)