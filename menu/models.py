from django.db import models

class Menu(models.Model):
    SEASONS = [
        ('winter', 'Зимнее'),
        ('spring', 'Весеннее'),
        ('summer', 'Летнее'),
        ('autumn', 'Осеннее'),
    ]
    dish=models.ManyToManyField("Dish")
    seasons=models.CharField(max_length=10, choices=SEASONS, default='summer')
class Restaurant(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    location=models.CharField(max_length=50)
class Employee(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='employees')
class Dish(models.Model):
    description=models.TextField(max_length=100)
    price=models.FloatField()
    currency=models.CharField(max_length=20)
    duration_of_cooking=models.DurationField()


