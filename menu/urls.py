from django.urls import path
import menu.views as views
app_name='menu'
urlpatterns=[
    path('menu_list/', views.dish_list, name='dish_list'),
    path("order/<int:pk>/", views.order_create, name="order_create"),
    path('dish/create/', views.CreateDish.as_view(), name='dish_create'),
    path('delete/<int:pk>', views.dish_delete, name='dish_delete'),
    path('update/', views.UpdateDish.as_view(), name='dish_update'),
]