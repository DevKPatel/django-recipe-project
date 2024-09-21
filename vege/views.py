from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        Recipe.objects.create(recipe_name = recipe_name, recipe_description = recipe_description, recipe_image = recipe_image)

        return redirect('/')
    context = {
        'title': "Home"
    }
    return render(request, "vege/index.html", context)

def view_recipes(request):
    recipes = Recipe.objects.all()
    if request.GET.get('search'):
        recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))
    context = {
        'recipes': recipes,
        'title': "View Recipes"
    }
    return render(request, "vege/view_recipes.html", context)
    
def update_recipe(request,id):
    recipe = Recipe.objects.get( id = id)
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description
        if recipe_image:
            recipe.recipe_image = recipe_image
        
        recipe.save()
        return redirect('/view_recipes')
    context = {
        'recipe' : recipe,
        'title': "Update Recipe"
    }
    return render(request, "vege/update_recipe.html", context)
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return redirect("/view_recipes")
        