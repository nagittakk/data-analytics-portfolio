'''
Inventory Manager

This program for a shoe store, allows users to update and access inventory data seamlessly. 
This project leverages object-oriented programming principles, enabling efficient organization 
and manipulation ofinventory items. The program streamlines inventory management with user-friendly 
interfaces, boosting operational efficiency.

'''

# import libraries
from tabulate import tabulate 

# --- Class --- #

# create Shoe class
class Shoe:

    # create constructor with attributes and their instances
    def __init__(self, country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # class method to return item cost
    def get_cost(self):

        print (f"Item cost: R {self.cost}") 

     # class method to return item quanity in inventory
    def get_quantity(self):

        print (f"Inventory quantity: {self.quantity}")

    # class method to return string representation of a class object
    def __str__(self):
         
        print (f'''
Product:    {self.product}
Country:    {self.country}
Code:       {self.code}
Cost:       R {self.cost}
Quantity:   {self.quantity}''')

shoe_list = [] # empty list to store shoes objects


# ---- Functions for inventory manager program ---- #


# function that reads shoe inventory information from inventory.txt file and creates shoe objects to store in the shoe_list
def read_shoes_data():

    # open inventory.txt file to read each line
    with open('inventory.txt', 'r') as inventory_file:
        item_line = inventory_file.readlines()
    
    # loop through each line in inventory.txt
    for item in item_line:
        temp = item.strip() # remove new line character
        temp = temp.split(',') # separate each word in line to have a separate index that can be used

        # create class object and append object to shoe_list
        shoe = Shoe(temp[0], temp[1], temp[2], temp[3], temp[4])
        shoe_list.append(shoe) 


# function for user to capture shoe data and create a shoe object that will be appended to the shoe list
def capture_shoes(): 

    # request user to input product details
    country = input("\nEnter the product location (country): ")
    code = input("\nEnter the product code: ")
    product = input("\nEnter the product name: ")
    cost = input("\nEnter the product cost (Rands): ")
    quantity = input("\nEnter the product quantity: ")
    
    # create class object
    shoe = Shoe(country,code,product,cost,quantity)

    # append captured product to inventory.txt 
    with open('inventory.txt', 'a+') as inventory_file: 
        inventory_file.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost}.00,{shoe.quantity}")
    
    print(f"\nProduct has been captured by Inventory Manager...") # display message after capture of product
    shoe.__str__() # call method to display details of captured product as a string


# funcion to display inventory data:
def view_all(): 

    # empty list to store lists of shoe data - used to make inventory table
    shoe_items = [['Country','Code','Product','Cost(R)','Quantity']]
    
    # loop through each object in the shoe_list
    for objct in shoe_list:

        # try exception block to 'get rid of' given headers and use entered headers (show currency in cost column)
        try:
            shoe_items.append([objct.country, objct.code, objct.product, int(objct.cost), objct.quantity ]) # append list to shoe_list
        except Exception:
            continue

    # display product data in inventory table
    print(f'''\n
                        ___Product Inventory___

{tabulate(shoe_items, headers = 'firstrow', tablefmt = 'fancy_grid')}''') 


# function that determines shoe with the lowest stock ,with the option to restock it
def re_stock():

    stock_qty = [] # empty list to store inventory quantities of each shoe  

    # loop through each object in the shoe_list
    for objct in shoe_list:    

        # try-except block to skip string 'Quantity' in quantity list when called as integer
        try:
            stock_qty.append(int(objct.quantity)) # append product quantity to stock_qty

        except Exception:
            continue

    lowest_stock = min(stock_qty) # determine poduct with lowest quantity

    lowest_index = stock_qty.index(lowest_stock) + 1 # determine index of product with lowest quantity - add 1 for 'Quantity' heading being gone

    lowest_shoe = shoe_list[lowest_index] # get the object with the lowest quantity from the shoe_list
    
    print(f'''\n
Product low in stock:  {lowest_shoe.product}
Quantity:              {lowest_shoe.quantity}''') # display message for product with lowest stock

    
    # while loop asking user whether they would like to resock the item
    while True:
        ans = input("\nWould you like to restock this item? (Enter 'Y' for yes, or 'N' for no, or 'e' to exit to main menu: ")

        # users answers 'yes' to restock the prooduct
        if ans.lower() == "y":
            
            # try-except block to prevent runtime erorr for non integer input by user (inside while loop)
            while True:
                ans2 = int(input(f"\nHow many units of this product would you like to restock? (Enter the number only): "))
               
                try:
                    new_qty = int(lowest_shoe.quantity) + ans2 # calculate product's new quantity - add new units to exiting units
                    shoe_list[lowest_index].quantity = new_qty # update quantity of lowest stock product in shoe_list

                    # update object in shoe_list
                    updated_shoe = shoe_list[lowest_index]
                    
                    # loop throuhgh shoe_list to overwrite inventory.txt file with updated data
                    for i in range(len(shoe_list)):

                        # condition to OVERWRITE inventory.txt file for first line of writing - WITH new line for next data
                        if i == 0: 
                            with open('inventory.txt', 'w+') as inventory_file: 
                                inventory_file.write(f"{shoe_list[i].country},{shoe_list[i].code},{shoe_list[i].product},{shoe_list[i].cost},{shoe_list[i].quantity}\n")

                        # condition to APPEND to inventory.txt file for the rest rest of the data - WITH new line for next data
                        elif i > 0 and i < (len(shoe_list)-1):
                            with open('inventory.txt', 'a+') as inventory_file: 
                                inventory_file.write(f"{shoe_list[i].country},{shoe_list[i].code},{shoe_list[i].product},{shoe_list[i].cost},{shoe_list[i].quantity}\n")
                        
                        # condition to APPEND to inventory.txt file for the last product - WITHOUT new line for next data
                        else: 
                            with open('inventory.txt', 'a+') as inventory_file: 
                                inventory_file.write(f"{shoe_list[i].country},{shoe_list[i].code},{shoe_list[i].product},{shoe_list[i].cost},{shoe_list[i].quantity}")
                        
                    print(f"\nInventory quantity of the product '{lowest_shoe.product}' has been updated to: {lowest_shoe.quantity}") # display message to user of updatae quantity

                    print(f'''
    Resotocked Item Summary''') # display heading for restocked item
                    
                    lowest_shoe.__str__() # display of restocked item details - class method
                    break 

                    
                except ValueError:
                    print("\n\nInvalid entry. Try again.") # displaty message for invalid entryby user
                    continue
            
            break

        # user answers 'no' to restock the product
        elif ans.lower() == "n":
            print (f"\nInventory stock of the product '{lowest_shoe.product}' has been left as: {lowest_shoe.quantity}.")
            break

        # user chooses to exit to the main menu
        elif ans.lower() == "e":
            break

        # user make invalid entry
        else:
            print("Invalid entry. Try again.") # display message for invalid entry
            continue


# function to search for product with product code as input/search criteria
def search_shoe():
    code = input("\nEnter the product code: ")

    codes = [] # list to store all product codes to check if they match the entered code
    
    # loop through each object in the shoe_list
    for objct in shoe_list:
        codes.append(objct.code) # append codes to code list

    # check if code entered is in code list
    # product code found
    if code in codes:        
        code_index = codes.index(code) # get the index of the code in the list
        found_objct = shoe_list[code_index] # get the object from the shoe_list using the code index
        print(f"\n--- Product found ---") # display message for found product
        found_objct.__str__() # display info of found product - class method
     
    # prodcut code not found  
    else:
        print(f"\nNo product exists with the code: {code}") # display message if product/code not found


# function to calculate total value of items in stock
def value_per_item():
    
    values = [['Product', 'Cost per unit (R)','Quantity ','Product Value (R)']] # empty list to store tot values - table headers as first row

    # loop through each object in the shoe_list
    for objct in shoe_list:

        # try-except block to 'get rid of' headers 'Product', 'Cost' and 'Quantity' - fail to cast as int (Error) - to inculde 4th header
        try:
            prod_val = int(objct.cost) * int(objct.quantity) # calculate product value = cost * quantity
            values.append([objct.product, objct.cost, objct.quantity, prod_val]) # append list of product, cost (per unit), quantity and product value to values list

        except Exception:
            continue   
        
    # display value per item data in a table
    print(f'''\n
                                Inventory Values\n''')
    print(tabulate(values, headers = "firstrow", tablefmt = "fancy_grid"))  # table displaying inventory total values
        

def highest_qty():

    stock_qty = [] # empty list to store inventory quantities of each shoe  

    for objct in shoe_list:

        # try-except block to skip string 'Quantity' in quantity list when called as integer
        try:
            stock_qty.append(int(objct.quantity)) # append product quantity to stock_qty

        except Exception:
            continue

    highest_stock = max(stock_qty) # determine poduct with highest quantity

    highest_index = stock_qty.index(highest_stock) + 1 # determine index of product with highest quantity - add 1 for 'Quantity' heading being gone

    highest_product = shoe_list[highest_index]

    print(f"\nProduct on sale: '{highest_product.product}'\n\nProduct details:") # display of product highest in quantity as being on sale
    highest_product.__str__() # display of product details - class method


# ---- Inventory manager progam ----

# menu - while loop with men options 
menu = True

while True:
    choice = input('''
        INVENTORY MANAGER

Select one of  the following options:

Capture new product            - np
View all inventory             - va
Restock items low in stock     - ri
Search for product             - sp
View inventory values          - iv
View product on sale           - ps
Exit                           - e
: ''') # displayed menu with options for various actions  
    
    # user chosses to capture a new product
    if choice.lower() == 'np':
        read_shoes_data() # call function to prepare shoe_list
        capture_shoes() # call function to captur new product

    # user chooses to capture a new product
    elif choice.lower() == 'va':
        read_shoes_data()
        view_all() # call function to view all inventory

    # user chooses to restock the item lowest in stock
    elif choice.lower() == 'ri':
        read_shoes_data()
        re_stock() # call function to restock item lowest in stock

    # user chooses to search for a product
    elif choice.lower() == 'sp':
        read_shoes_data()
        search_shoe() # call function to search for item

    # user chooses to view the inventory values
    elif choice.lower() == 'iv':
        read_shoes_data()
        value_per_item() # call function to view inventory values

    # user chooes to view the product that's on sale
    elif choice.lower() == 'ps':
        read_shoes_data()
        highest_qty() # call function to view product on sale

    # user chooses to exit
    elif choice.lower() == 'e':
        print("You have been logged out. Goodbye!") # exit display message 
        break
        
    # user entry invalid
    else:
        print("\nOops! Invalid entry. Try again.") # invalid entry display message