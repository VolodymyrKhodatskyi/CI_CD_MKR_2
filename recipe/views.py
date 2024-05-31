from django.shortcuts import render
from recipe.models import Recipe, Category

def main(request):
    Recipe.objects.create(title="Test", description="Test", instructions="Test", ingredients="Test")
    recipes =   Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'main.html', context)



def category_list(request):
    Category.objects.create(name="Test1")
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)