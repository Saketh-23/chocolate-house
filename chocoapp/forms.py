# chocoapp/forms.py
from django import forms
from .models import Flavor, Ingredient, CustomerSuggestion

class FlavorForm(forms.ModelForm):
    class Meta:
        model = Flavor
        fields = ['name', 'description', 'is_seasonal']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['customer_name', 'suggested_flavor', 'allergy_concern']
