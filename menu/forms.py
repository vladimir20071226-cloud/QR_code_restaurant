from django.contrib.auth.models import User
from django import forms
from .models import Dish
class RegisterForm(forms.Form):
    class Meta:
        model=User
        fields=['username', 'password', 'email']
class DishForm(forms.Form):
    class Meta:
        model=Dish
        values=['description', 'currency', 'price', 'duration_of_cooking']