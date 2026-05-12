class Cart:
    def __init__(self, request):
        self.session=request.session
        cart=request.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart=cart
    def add(self, dish, quantity):
        dish_id=str(dish.id)
        if dish_id not in self.cart:
            self.cart[dish_id]={"id": dish.id, "name": dish.name, "price": float(dish.price), "quantity": 0}
        self.cart[dish_id]["quantity"]+=quantity
        self.save()
    def remove(self, dish):
        dish_id=str(dish.id)
        if dish_id not in self.cart:
            del self.cart[dish_id]
            self.save()
    def clear(self):
        self.session['cart'] = {}
        self.save()
    def save(self):
        self.session.modified=True