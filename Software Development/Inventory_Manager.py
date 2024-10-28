'''
Inventory Manager

This program for a shoe store allows users to update and access inventory data seamlessly. 
This project leverages object-oriented programming principles, enabling efficient organization 
and manipulation of inventory items. The program streamlines inventory management with user-friendly 
interfaces, boosting operational efficiency.
'''

# Import necessary libraries
from tabulate import tabulate

# --- Class Definitions --- #

class Shoe:
    """Class representing a shoe item in the inventory."""
    
    def __init__(self, country, code, product, cost, quantity):
        """
        Initialize a Shoe object with the given attributes.

        Parameters:
        country (str): The country where the shoe is made.
        code (str): The unique product code.
        product (str): The name of the product.
        cost (float): The cost of the shoe.
        quantity (int): The available quantity in stock.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Return the cost of the shoe."""
        print(f"Item cost: R {self.cost}")

    def get_quantity(self):
        """Return the available quantity of the shoe in inventory."""
        print(f"Inventory quantity: {self.quantity}")

    def __str__(self):
        """Return a string representation of the shoe object."""
        return (f'''
Product:    {self.product}
Country:    {self.country}
Code:       {self.code}
Cost:       R {self.cost}
Quantity:   {self.quantity}''')

# Initialize an empty list to store shoe objects
shoe_list = []


# ---- Functions for Inventory Manager Program ---- #

def read_shoes_data():
    """Read shoe inventory data from a file and populate the shoe_list."""
    # Open the inventory file to read each line
    with open('inventory.txt', 'r') as inventory_file:
        item_lines = inventory_file.readlines()
    
    # Loop through each line in the inventory file
    for item in item_lines:
        temp = item.strip().split(',')  # Remove new line characters and split line into components
        # Create a Shoe object and append it to the shoe_list
        shoe = Shoe(temp[0], temp[1], temp[2], float(temp[3]), int(temp[4]))
        shoe_list.append(shoe)

def capture_shoes():
    """Capture new shoe data from user input and append to the shoe list."""
    # Request user to input product details
    country = input("\nEnter the product location (country): ")
    code = input("\nEnter the product code: ")
    product = input("\nEnter the product name: ")
    cost = float(input("\nEnter the product cost (Rands): "))
    quantity = int(input("\nEnter the product quantity: "))
    
    # Create a Shoe object
    shoe = Shoe(country, code, product, cost, quantity)

    # Append captured product to inventory.txt 
    with open('inventory.txt', 'a+') as inventory_file: 
        inventory_file.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")

    print(f"\nProduct has been captured by Inventory Manager...")  # Display confirmation message
    print(shoe)  # Display details of captured product as a string

def view_all():
    """Display all shoes in inventory in a tabular format."""
    # Prepare the header for the inventory table
    shoe_items = [['Country', 'Code', 'Product', 'Cost (R)', 'Quantity']]
    
    # Loop through each object in the shoe_list
    for obj in shoe_list:
        # Append shoe data to shoe_items for display
        shoe_items.append([obj.country, obj.code, obj.product, obj.cost, obj.quantity])

    # Display product data in inventory table
    print(f'''\n
                        ___Product Inventory___

{tabulate(shoe_items, headers='firstrow', tablefmt='fancy_grid')}''')

def re_stock():
    """Determine the shoe with the lowest stock and provide an option to restock it."""
    stock_qty = []  # List to store quantities of each shoe  

    # Loop through each object in the shoe_list
    for obj in shoe_list:
        stock_qty.append(obj.quantity)  # Append product quantity to stock_qty

    # Find the index of the shoe with the lowest stock
    lowest_index = stock_qty.index(min(stock_qty)) 
    lowest_shoe = shoe_list[lowest_index]  # Get the shoe object with the lowest quantity

    # Display details of the shoe low in stock
    print(f'''\n
Product low in stock:  {lowest_shoe.product}
Quantity:              {lowest_shoe.quantity}''')

    # Prompt user to restock the item
    while True:
        ans = input("\nWould you like to restock this item? (Enter 'Y' for yes, 'N' for no, or 'e' to exit): ")

        if ans.lower() == "y":
            # Prompt user for the number of units to restock
            while True:
                try:
                    ans2 = int(input(f"\nHow many units of this product would you like to restock? (Enter the number only): "))
                    # Update quantity of the shoe
                    lowest_shoe.quantity += ans2
                    print(f"\nInventory quantity of '{lowest_shoe.product}' has been updated to: {lowest_shoe.quantity}")

                    # Overwrite inventory.txt with updated data
                    with open('inventory.txt', 'w') as inventory_file:
                        for shoe in shoe_list:
                            inventory_file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

                    print(f"\nRestocked Item Summary")
                    print(lowest_shoe)  # Display details of restocked item
                    break 

                except ValueError:
                    print("\nInvalid entry. Please enter a valid number.")  # Handle invalid input
            break

        elif ans.lower() == "n":
            print(f"\nInventory stock of '{lowest_shoe.product}' remains: {lowest_shoe.quantity}.")
            break

        elif ans.lower() == "e":
            break

        else:
            print("Invalid entry. Please try again.")  # Handle invalid input

def search_shoe():
    """Search for a shoe product by its code."""
    code = input("\nEnter the product code: ")
    codes = [obj.code for obj in shoe_list]  # Create a list of product codes

    # Check if the entered code is in the codes list
    if code in codes:
        code_index = codes.index(code)  # Get the index of the found code
        found_obj = shoe_list[code_index]  # Get the corresponding shoe object
        print(f"\n--- Product found ---")
        print(found_obj)  # Display details of the found product
    else:
        print(f"\nNo product exists with the code: {code}")  # Handle code not found

def value_per_item():
    """Calculate and display the total value of items in stock."""
    values = [['Product', 'Cost per unit (R)', 'Quantity', 'Product Value (R)']]  # Prepare headers for value table

    # Loop through each object in the shoe_list
    for obj in shoe_list:
        prod_val = obj.cost * obj.quantity  # Calculate product value
        values.append([obj.product, obj.cost, obj.quantity, prod_val])  # Append product details to values list

    # Display value per item data in a table
    print(f'''\n
                                Inventory Values\n''')
    print(tabulate(values, headers="firstrow", tablefmt="fancy_grid"))  # Display inventory total values

def highest_qty():
    """Find and display the product with the highest stock quantity."""
    stock_qty = [obj.quantity for obj in shoe_list]  # Create a list of quantities

    highest_index = stock_qty.index(max(stock_qty))  # Get the index of the highest quantity
    highest_product = shoe_list[highest_index]

    print(f"\nProduct on sale: '{highest_product.product}'\n\nProduct details:")  # Display product on sale
    print(highest_product)  # Display details of the highest quantity product


# ---- Inventory Manager Program ----

# Menu loop with options for various actions
while True:
    choice = input('''
        INVENTORY MANAGER

Select one of the following options:

Capture new product            - np
View all inventory             - va
Restock items low in stock     - ri
Search for product             - sp
View inventory values          - iv
View product on sale           - ps
Exit                           - e
: ''')  # Display menu with options

    # User choices
    if choice.lower() == 'np':
        read_shoes_data()  # Prepare shoe_list from file
        capture_shoes()  # Capture a new product

    elif choice.lower() == 'va':
        read_shoes_data()  # Prepare shoe_list from file
        view_all()  # Display all inventory

    elif choice.lower() == 'ri':
        read_shoes_data()  # Prepare shoe_list from file
        re_stock()  # Restock item low in stock

    elif choice.lower() == 'sp':
        read_shoes_data()  # Prepare shoe_list from file
        search_shoe()  # Search for a product

    elif choice.lower() == 'iv':
        read_shoes_data()  # Prepare shoe_list from file
        value_per_item()  # Display total values per item

    elif choice.lower() == 'ps':
        read_shoes_data()  # Prepare shoe_list from file
        highest_qty()  # Display product with highest quantity

    elif choice.lower() == 'e':
        print("Exiting Inventory Manager. Goodbye!")  # Exit message
        break  # Exit the menu loop

    else:
        print("Invalid option. Please try again.")  # Handle invalid input
