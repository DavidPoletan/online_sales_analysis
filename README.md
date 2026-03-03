This project contains a system used for sales data analysis of an imaginary online store.

It's split into four differnet Python scripts: product.py, product_manager.py, cart.py and main.py.

The product.py script contains the Product class. It's used to initialize a single instance of the Product class which represents a product in our online store. When initializing an object of the Product class, the user sets the name, price and quantity of a product they wish to add.
The display_info method of this class is used to display the parameters(name, price and quantity) the user has set.
The update_quantity method of this class is used to set a new quantity for a given product and get_quantity method serves as a getter for the updated value.

The product_manager.py script contains the ProductManager class. Object of this class is a list in which user adds/removes products.
The add_product method is used to append a Product object to the list.
The remove_product method is used to remove products from the list by their name.
The display_list method incorporates the display_info method of the Product class to display all products that are on the list.
The total_price method returns the total value of every single unit of all the products that are on the list.

The cart.py script contains th Cart class. Object of this class is also a list, but it contains the products that a customer wishes to purchase.
The add_items method is used to add a product to the cart.
The cart_price method returns the tootal value of all the products that are in the cart.
The display_cart is used to display all the products that are currently in the cart.

The main.py is the main script with which the user interacts. It imports all previously mentioned scripts and presents multiple choices to the user. Each choice represents an action which manipulates/analyzes the data using diffenrent methods.