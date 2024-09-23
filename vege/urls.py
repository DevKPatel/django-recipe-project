from django.urls import path
from . import views
urlpatterns = [
    path('',views.recipes, name = "recipes" ),
    path('view_recipes', views.view_recipes, name = "view_recipes"),
    path('delete_recipe/<int:id>', views.delete_recipe, name = "delete_recipe"),
    path('update_recipe/<int:id>', views.update_recipe, name = "update_recipe"),
    path('login', views.login_page, name = "login"),
    path('register', views.register_page, name = "register"),
    path('logout', views.logout_page, name = "logout"),
]