from product import Product
from product_manager import ProductManager

productsList = ProductManager()

product1 = Product("Laptop", 979.99, 15)
product2 = Product("Keyboard", 57.95, 21)
product3 = Product("Mouse", 32, 17)
product4 = Product("Headphones", 91.99, 7)

productsList.add_product(product1); productsList.add_product(product2); productsList.add_product(product3); productsList.add_product(product4)

print("===== Product Manager =====")

while True:

    print("1) Show a list of all current products")
    print("2) Show total price of all current products")
    print("3) Add a new product to the list")
    print("4) Remove a product from the list")
    print("5) Exit\n")

    choice = input("Choose an option (1-5): ").strip()
    print()

    if choice == "1":

        productsList.display_list()
        print("\n===============\n\n")


    elif choice == "2":

        print(f"Total price of all current products is: {productsList.total_price():.2f}")
        print("\n===============\n\n")



    elif choice == "3":

        print("Adding a new product: ")
        new_product_name =     input("New product name:     ")
        new_product_price =    float(input("New product price:    "))
        new_product_quantity = int(input("New product quantity: "))

        new_product = Product(new_product_name, new_product_price, new_product_quantity)

        productsList.add_product(new_product)
        print("\n===============\n\n")


    elif choice == "4":

        to_be_removed = input("Enter the name of the product you wish to remove: ").strip()
        productsList.remove_product(to_be_removed)
        print("\n===============\n\n")


    elif choice == "5":

        print("\nGoodbye!\n")
        break