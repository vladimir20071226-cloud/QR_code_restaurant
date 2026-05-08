from django.db import models
class Dish(models.Model):
    description=models.TextField(blank=True, default="")
    price=models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    currency=models.CharField(default="KZT")
    cook_time=models.IntegerField(default=0, help_text="Время готовки в минутах")
    image=models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    SEASONS = [
        ('winter', 'Зимнее'),
        ('spring', 'Весеннее'),
        ('summer', 'Летнее'),
        ('autumn', 'Осеннее'),
    ]
    dish=models.ManyToManyField("Dish")
    seasons=models.CharField(max_length=10, choices=SEASONS, default='summer')
    def __str__(self):
        return f"Mеню - {self.get_seasons_display()}"
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
    def __str__(self):
       return f"{self.name} - {self.position}"


