# chocoapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('flavors/', views.flavor_list, name='flavor_list'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('suggestions/', views.suggestion_list, name='suggestion_list'),
    path('add_flavor/', views.add_flavor, name='add_flavor'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('add_suggestion/', views.add_suggestion, name='add_suggestion'),
]
