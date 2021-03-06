from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id, is_published=True).order_by('-id')

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id'))

    return render(request, 'recipes/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category'
    })


def recipes(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
