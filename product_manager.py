from product import Product

class ProductManager(Product):

    def __init__(self):

        self.products_list = []

    
    def add_product(self, product:Product):

        self.products_list.append(product)
        return self.products_list
    

    def display_list(self):

        i = 1

        print("List of all current products: ")

        for product in self.products_list:

            print(f"Product no.{i}: ")
            product.display_info()
            i += 1


    def total_price(self):

        totalPrice = 0.0
        
        for product in self.products_list:

            totalPrice += (product.price * product.quantity)

        return totalPrice