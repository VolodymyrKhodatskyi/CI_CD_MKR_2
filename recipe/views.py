from django.shortcuts import render
from recipe.models import Recipe, Category

def main(request):
    recipes = Recipe.objects.order_by('-created_at')[:5]
    context = {'recipes': recipes}
    return render(request, 'main.html', context)



def category_list(request):
    categories = Category.objects.order_by()[:5]
    context = {'categories': categories}
    return render(request, 'category_list.html', context)