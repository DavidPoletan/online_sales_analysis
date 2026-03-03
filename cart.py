from product import Product

class Cart(Product):

    def __init__(self):
        
        self.cart_items = []


    def add_items(self, product:Product):

        self.cart_items.append(product)
        return self.cart_items