from product import Product
from product_manager import ProductManager

productsList = ProductManager()

product1 = Product("Laptop", 979.99, 15)
product2 = Product("Keyboard", 57.95, 21)
product3 = Product("Mouse", 32, 17)
product4 = Product("Headphones", 91.99, 7)

product1.update_quantity(27); product4.update_quantity(13)

productsList.add_product(product1); productsList.add_product(product2); productsList.add_product(product3); productsList.add_product(product4)

print("===== Product Manager =====")

while True:

    print("1) Add a new producct to the current products list")
    print("2) Remove a existing product from the current products list")
    print("3) Exit\n")

    choice = input("Choose an option (1-3): ").strip()
    print()

    if choice == "1":

        print("Adding a new product: ")
        new_product_name =     input("New product name:     ")
        new_product_price =    float(input("New product price:    "))
        new_product_quantity = int(input("New product quantity: "))

        new_product = Product(new_product_name, new_product_price, new_product_quantity)

        productsList.add_product(new_product)
        print("\n===============\n\n")


    elif choice == "2":

        to_be_removed = input("Enter the name of the product you wish to remove: ").strip()
        productsList.remove_product(to_be_removed)
        print("\n===============\n\n")


    elif choice == "3":

        print("\nGoodbye!\n")
        break