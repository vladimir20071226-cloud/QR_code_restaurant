from django.contrib import admin
from .models import Dish, Menu, Restaurant, Employee, Order, OrderItem
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display=("description", "cook_time", "price", "currency", "image")
    list_filter=("currency",)
    search_fields=("description",)
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="height:50px;"/>'
        return "Нет фото"
    image_preview.allow_tags = True
    image_preview.short_description = "Фото"
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=("season",)
    filter_horizontal=("dish",)
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=("title", "location",)
    search_fields=("title",)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=("name", "position", "restaurant", "image")
    search_fields=("position", "restaurant",)
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="height:50px;"/>'
        return "Нет фото"
    image_preview.allow_tags = True
    image_preview.short_description = "Фото"
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=("customer_name", "phone", "created_at", "status",)
    list_filter=("status", "created_at",)
    search_fields=("items__dish__name", "customer_name", "phone",)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=("dish", "order", "quantity",)
    list_filter=("order",)


