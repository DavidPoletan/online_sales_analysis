class Product:

    def __init__(self, name, price, quantity):

        self.name =     name
        self.price =    price
        self.quantity = quantity


    def display_info(self):

        print(f"Product name:     {self.name}")
        print(f"Product price:    {self.price:.2f}")
        print(f"Product quantity: {self.quantity}")
        print()

    
    def update_quantity(self, upd_quantity):

        if upd_quantity >= 0:

            self.quantity = upd_quantity

        else:

            print("Quantity cannot be a negative number!")


    def get_quantity(self): return self.quantity