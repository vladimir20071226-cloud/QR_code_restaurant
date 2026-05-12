from django.shortcuts import render,redirect, get_object_or_404
from .forms import DishForm
from .models import Dish, Employee, Order, OrderItem
from django.views import View
from .cart import Cart


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu_detail.html', {'dishes': dishes})
def order_success(request, order_id):
    order=get_object_or_404(Order, pk=order_id)
    return render(request, "order_success.html", {"order": order})

def order_create(request, pk):
    dish=get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        order=Order.objects.create(phone=request.POST.get("phone"),
                                   customer_name=request.POST.get("customer_name"),
                                   status="new")

        OrderItem.objects.create(
            order=order,
            dish=dish,
            quantity=request.POST.get("quantity", 1)
        )
        return redirect("menu:order_success", order_id=order.id)
    return render(request, "order_form.html", {"dish": dish})
def cart_detail(request):
    orders=Order.objects.order_by("-created_at")
    return render(request, "cart_detail.html", {"orders": orders})
def dish_delete(request, pk):
    dish = Dish.objects.get(pk=pk)
    dish.delete()
    return redirect('dish_list')
def restaurant_info(request):
    return render(request, "restaurant_info.html")
def add_to_cart(request, pk):
    dish=get_object_or_404(Dish, pk=pk)
    cart=Cart(request)
    cart.add(dish, quantity=int(request.POST.get("quantity", 1)))
    return redirect("menu:cart_detail")
def remove_from_cart(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    cart=Cart(request)
    cart.remove(dish)
    return redirect("menu:cart_detail")
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee_list.html", {"employees": employees})
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
