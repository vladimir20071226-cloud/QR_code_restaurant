from django.contrib import admin
from .models import Dish, Menu, Restaurant, Employee
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display=("description", "cook_time", "price", "currency", "image")
    list_filter=("currency",)
    search_fields=("description",)
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=("seasons",)
    filter_horizontal=("dish",)
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=("title", "location",)
    search_fields=("title",)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=("name", "position", "restaurant")
    search_fields=("position", "restaurant",)

# Register your models here.
