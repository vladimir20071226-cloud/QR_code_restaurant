from django.db import models
from django.contrib.auth.models import User
class Menu(models.Model):
    SEASONS = [
        ('winter', 'Зимнее'),
        ('spring', 'Весеннее'),
        ('summer', 'Летнее'),
        ('autumn', 'Осеннее'),
    ]
    dish=models.ManyToManyField("Dish", related_name="menus")
    season = models.CharField(max_length=10, choices=SEASONS, default="summer")
    def __str__(self):
        return f"Mеню - {self.get_season_display()}"
class Dish(models.Model):
    name = models.CharField(max_length=100, default="Без названия")
    description=models.TextField(blank=True, default="")
    price=models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    currency=models.CharField(default="KZT")
    cook_time=models.IntegerField(default=0, help_text="Время готовки в минутах")
    image=models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    location=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Employee(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='employees')
    image=models.ImageField(upload_to='employees/', blank=True, null=True)
    def __str__(self):
       return f"{self.name} - {self.position}"
class Order(models.Model):
    STATUS_CHOICES=[("new", "новый"),
                    ("in_progress", "в процессе"),
                    ("done", "готово")
                    ]
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Заказ №{self.id} — {self.dish.name}"
class OrderItem(models.Model):
    dish=models.ForeignKey("Dish", on_delete=models.CASCADE, related_name='items')
    quantity=models.PositiveIntegerField(default=1)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"

