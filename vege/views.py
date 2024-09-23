from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url= '/login')
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
@login_required(login_url= '/login')
def view_recipes(request):
    recipes = Recipe.objects.all()
    if request.GET.get('search'):
        recipes = recipes.filter(recipe_name__icontains = request.GET.get('search'))
    context = {
        'recipes': recipes,
        'title': "View Recipes"
    }
    return render(request, "vege/view_recipes.html", context)

@login_required(login_url= '/login')
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
@login_required(login_url= '/login')
def delete_recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return redirect("/view_recipes")

def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/')
    context = {
        'title': "Login Page"
    }
    return render(request, "vege/login.html", context)

def logout_page(request):
    logout(request)
    return redirect('/login')

def register_page(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        check_user = User.objects.filter(username = username)
        if check_user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register')
        user =User.objects.create_user(first_name = first_name, last_name = last_name, username = username)
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('/login')
    context = {
        'title': "Register Page"
    }
    return render(request, "vege/register.html", context)
        