from product import Product

class Cart(Product):

    def __init__(self):
        
        self.cart_items = []


    def add_items(self, product:Product):

        self.cart_items.append(product)
        return self.cart_items
    

    def cart_price(self):

        cartPrice = 0

        for product in self.cart_items:

            cartPrice += product.price

        return cartPrice
    

    def display_cart(self):

        i = 1

        print("List of products added to the cart: ")

        for product in self.cart_items:

            print(f"{i}. {product.name}")
            i += 1