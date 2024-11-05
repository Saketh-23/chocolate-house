# chocoapp/views.py
from django.shortcuts import render, redirect
from .models import Flavor, Ingredient, CustomerSuggestion
from .forms import FlavorForm, IngredientForm, SuggestionForm

def flavor_list(request):
    flavors = Flavor.objects.all()
    return render(request, 'chocoapp/flavor_list.html', {'flavors': flavors})

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'chocoapp/ingredient_list.html', {'ingredients': ingredients})

def suggestion_list(request):
    suggestions = CustomerSuggestion.objects.all()
    return render(request, 'chocoapp/suggestion_list.html', {'suggestions': suggestions})

def add_flavor(request):
    if request.method == 'POST':
        form = FlavorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flavor_list')
    else:
        form = FlavorForm()
    return render(request, 'chocoapp/add_flavor.html', {'form': form})

def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'chocoapp/add_ingredient.html', {'form': form})

def add_suggestion(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suggestion_list')
    else:
        form = SuggestionForm()
    return render(request, 'chocoapp/add_suggestion.html', {'form': form})

def home(request):
    return render(request, 'chocoapp/home.html')