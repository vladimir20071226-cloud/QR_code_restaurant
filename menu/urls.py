from django.urls import path
import menu.views as views
app_name='menu'
urlpatterns = [
    path('menu_list/', views.dish_list, name='dish_list'),
    path("order/<int:pk>", views.order_create, name="order_create"),
    path('dish/create/', views.CreateDish.as_view(), name='dish_create'),
    path('delete/<int:pk>/', views.dish_delete, name='dish_delete'),
    path('update/<int:pk>/', views.UpdateDish.as_view(), name='dish_update'),
    path('employees/', views.employee_list, name='employee_list'),
    # path("<str:season>/", views.seasonal_menu, name="seasonal_menu"),
    path("order/success/<int:order_id>", views.order_success, name="order_success"),
    path('restaurant_info/', views.restaurant_info, name='restaurant_info'),
    path('cart/', views.cart_detail, name="cart_detail"),
    path('cart/add/<int:pk>/', views.add_to_cart, name='cart_add'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
]