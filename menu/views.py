from django.shortcuts import render,redirect, get_object_or_404
from .forms import DishForm
from .models import Dish
from django.views import View



def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu_detail.html', {'menu_list': dishes})

def order_create(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'order_detail.html', {'dish': dish})

def dish_delete(request, pk):
    dish = Dish.objects.get(pk=pk)
    dish.delete()
    return redirect('dish_list')


class CreateDish(View):
    template_name = 'form.html'
    form_class = DishForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form, "form_title": "Добавить блюдо"})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
        return render(request, self.template_name, {"form": form, "form_title": "Добавить блюдо"})


class UpdateDish(View):
    template_name = 'form.html'
    form_class = DishForm

    def get(self, request, pk, *args, **kwargs):
        dish = get_object_or_404(Dish, pk=pk)
        form = self.form_class(instance=dish)
        return render(request, self.template_name, {"form": form, "form_title": "Редактировать блюдо"})

    def post(self, request, pk, *args, **kwargs):
        dish = get_object_or_404(Dish, pk=pk)
        form = self.form_class(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect("dish_detail", pk=dish.pk)
        return render(request, self.template_name, {"form": form, "form_title": "Редактировать блюдо"})
