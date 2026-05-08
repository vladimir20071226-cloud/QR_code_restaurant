from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Dish
from django.urls import reverse
from .forms import DishForm
class DishModelTest(TestCase):
    def test_create_dish(self):
        image = SimpleUploadedFile('test.jpg', b'file_content' ,content_type='image/jpeg')
        dish=Dish.objects.create(description="Тестовое блюдо",
                                 price=100,
                                 currency="KZT",
                                 cook_time=15,
                                 image=image
                                 )
        self.assertEqual(dish.price, 100)
        self.assertEqual(dish.currency, "KZT")
        self.assertEqual(dish.cook_time, 15)
        self.asserEqual(dish.image)
        self.assertEqual(dish.image.url)
class DishViewsTest(TestCase):
    def setUp(self):
        self.dish=Dish.objects.create(description="Тестовое блюдо",
                                 price=100,
                                 currency="KZT",
                                 cook_time=15
                                 )
    def test_dish_list_view(self):
        response=self.client.get(reverse("dish_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовое блюдо')
    def test_dish_detail_view(self):
        response=self.client.get(reverse("dish_detail"), args=[self.dish.pk])
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовое блюдо")
    def test_dish_detail_not_found(self):
        response=self.client.get(reverse("dish_detail"), args=[999])
        self.assertEqual(response.status_code, 404)
class DishFormTest(TestCase):
    def setUp(self):
        data={"description":"Тестовое блюдо",
              "price":100,
              "currency":"KZT",
              "cook_time":15}
        form=DishForm(data=data)
        self.assertTrue(form.is_valid())
        dish=form.save()
        self.assertEqual(dish.description, "Тестовое блюдо")
        self.assertEqual(dish.price, 100)
    def test_invalid_form_negative_price(self):
        data={"description":"Тестовое блюдо",
            "price":-50,
            "currency":"KZT",
            "cook_time":15}
        form=DishForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)
