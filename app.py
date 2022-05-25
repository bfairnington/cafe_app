# Packages
import pymysql
import csv

# Print functions
def print_products():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Extract table
    print('\nID, Name, Price, Inventory')
    cursor.execute(f'SELECT * FROM products') # SQL code
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
    print('\n')
    # Close cursor
    cursor.close() 
    # Close DB
    db.close() 

def print_couriers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Extract table
    print('\nID, Name, Phone')
    cursor.execute(f'SELECT * FROM couriers') # SQL code
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]}')
    print('\n')
    # Close cursor
    cursor.close() 
    # Close DB
    db.close() 

def print_orders():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Extract table
    print('\nID, Name, Address, Phone, Courier, Status, Items')
    cursor.execute(f'SELECT * FROM orders') # SQL code
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}')
    print('\n')
    # Close cursor
    cursor.close() 
    # Close DB
    db.close() 

def print_listed_orders(): # This is to list orders by category
    print('\nID,Name,Address,Phone,Courier,Status,Items\n')
    orders_list = input('\nSelect which category to list orders by\n') # Select the category to list orders
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Extract table
    print('\nID, Name, Address, Phone, Courier, Status, Items')
    cursor.execute(f'SELECT * FROM orders ORDER BY {orders_list}') # SQL code
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}')
    print('\n')
    # Close cursor
    cursor.close() 
    # Close DB
    db.close() 

def print_customers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Extract table
    print('\nID, Name, Phone')
    cursor.execute(f'SELECT * FROM customers') # SQL code
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]}')
    print('\n')
    # Close cursor
    cursor.close() 
    # Close DB
    db.close() 


# Add functions
def add_products():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_products()
    id = int(input("\nEnter new product id\n")) # User input id
    name = str(input("\nEnter new product name\n")) # User input name
    price = float(input("\nEnter new product price\n")) # User input price
    inventory = int(input("\nEnter new product inventory\n")) # User input inventory
    sql = "INSERT INTO products VALUES (%s, %s, %s, %s)" # SQL code
    cursor.execute(sql, (f'{id}', f'{name}', f'{price}', f'{inventory}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nProduct added\n')

def add_couriers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_couriers()
    id = int(input("\nEnter new courier id\n")) # User input id
    name = str(input("\nEnter new courier name\n")) # User input name
    phone = str(input("\nEnter new courier phone number\n")) # User input phone number
    sql = "INSERT INTO couriers VALUES (%s, %s, %s)" # SQL code
    cursor.execute(sql, (f'{id}', f'{name}', f'{phone}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nCourier added\n')

def add_orders():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_orders()
    id = int(input("\nEnter new order id\n")) # User input id
    name = str(input("\nEnter new order name\n")) # User input name
    address = str(input("\nEnter new order address\n")) # User input address
    phone = str(input("\nEnter new order phone\n")) # User input phone
    courier = int(input("\nEnter new order courier\n")) # User input courier
    status = str(input("\nEnter new order status\n")) # User input status
    items = str(input("\nEnter new order items\n")) # User input items
    sql = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s, %s, %s)" # Select
    cursor.execute(sql, (f'{id}', f'{name}', f'{address}', f'{phone}', f'{courier}', f'{status}', f'{items}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nOrder added\n')

def add_customers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_customers()
    id = int(input("\nEnter new customer id\n")) # User input id
    name = str(input("\nEnter new customer name\n")) # User input name
    phone = str(input("\nEnter new customer phone number\n")) # User input phone number
    sql = "INSERT INTO customers VALUES (%s, %s, %s)" # SQL code
    cursor.execute(sql, (f'{id}', f'{name}', f'{phone}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nCustomer added\n')


# Edit functions
def edit_products():
      # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_products()
    # Delete old product
    id = int(input("\nEnter product ID to edit\n")) # User input
    sql = f"DELETE FROM products WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    # Add new product
    name = str(input("\nEnter new product name\n")) # User input name
    price = float(input("\nEnter new product price\n")) # User input price
    inventory = int(input("\nEnter new product inventory\n")) # User input inventory
    sql = "INSERT INTO products VALUES (%s, %s, %s, %s)" # SQL code
    cursor.execute(sql, (f'{id}', f'{name}', f'{price}', f'{inventory}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nProduct updated\n')

def edit_couriers():
      # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_couriers()
    # Delete old courier
    id = int(input("\nEnter couier ID to edit\n")) # User input
    sql = f"DELETE FROM couriers WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    # Add new courier
    name = str(input("\nEnter new courier name\n")) # User input name
    phone = str(input("\nEnter new courier phone number\n")) # User input phone number
    sql = "INSERT INTO couriers VALUES (%s, %s, %s)" # SQL code
    cursor.execute(sql, (f'{id}', f'{name}', f'{phone}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nCourier updated\n')

def edit_orders():
      # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_orders()
    # Delete old order
    id = int(input("\nEnter order ID to edit\n")) # User input
    sql = f"DELETE FROM orders WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    # Add new order
    name = str(input("\nEnter new order name\n")) # User input name
    address = str(input("\nEnter new order address\n")) # User input address
    phone = str(input("\nEnter new order phone\n")) # User input phone
    courier = int(input("\nEnter new order courier\n")) # User input courier
    status = str(input("\nEnter new order status\n")) # User input status
    items = str(input("\nEnter new order items\n")) # User input items
    sql = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s, %s, %s)" # Select
    cursor.execute(sql, (f'{id}', f'{name}', f'{address}', f'{phone}', f'{courier}', f'{status}', f'{items}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nOrder updated\n')

def edit_order_status():
      # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_orders()
    # Update order status
    id = int(input("\nEnter order ID to update\n")) # User input
    status = str(input("\nEnter new order status\n")) # User input status
    sql = f"UPDATE orders SET status = '{status}' WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nOrder status updated\n')

def edit_customers():
      # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_customers()
    # Delete old customer
    id = int(input("\nEnter customer ID to edit\n")) # User input
    sql = f"DELETE FROM customers WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    # Add new customer
    name = str(input("\nEnter new customer name\n")) # User input name
    phone = str(input("\nEnter new customer phone number\n")) # User input phone number
    sql = "INSERT INTO customers VALUES (%s, %s, %s)" # SQL code
    cursor.execute(sql, (f'{id}', f'{name}', f'{phone}')) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nCustomer updated\n')


# Delete functions
def delete_products():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_products()
    id = int(input("\nEnter product ID to delete\n")) # User input
    sql = f"DELETE FROM products WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nProduct deleted\n')

def delete_couriers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_couriers()
    id = int(input("\nEnter courier ID to delete\n")) # User input
    sql = f"DELETE FROM couriers WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nCourier deleted\n')

def delete_orders():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_orders()
    id = int(input("\nEnter order ID to delete\n")) # User input
    sql = f"DELETE FROM orders WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nOrder deleted\n')

def delete_customers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
        ) 
    cursor = db.cursor() # Open cursor
    print_customers()
    id = int(input("\nEnter customer ID to delete\n")) # User input
    sql = f"DELETE FROM customers WHERE id = %s" # Select
    cursor.execute(sql, id) # Execute
    db.commit() # Commit change
    cursor.close() # Close cursor
    db.close() # Close DB
    print('\nCustomer deleted\n')


# Export functions
def export_products():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Define products list from DB
    products = []
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        products.append(row)
    cursor.close() # Close cursor
    db.close() # Close DB
    #  Export to products.csv
    with open('products.csv', mode='w', newline = '') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['ID','Name','Price', 'Inventory'])
        for i in range(0,len(products)):
            writer.writerow(products[i])

def export_couriers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Define couriers list from DB
    couriers = []
    cursor.execute('SELECT * FROM couriers')
    rows = cursor.fetchall()
    for row in rows:
        couriers.append(row)
    cursor.close() # Close cursor
    db.close() # Close DB
    #  Export to couriers.csv
    with open('couriers.csv', mode='w', newline = '') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['ID','Name','Phone'])
        for i in range(0,len(couriers)):
            writer.writerow(couriers[i])

def export_orders():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Define orders list from DB
    orders = []
    cursor.execute('SELECT * FROM orders')
    rows = cursor.fetchall()
    for row in rows:
        orders.append(row)
    cursor.close() # Close cursor
    db.close() # Close DB
    #  Export to orders.csv
    with open('orders.csv', mode='w', newline = '') as file:
        writer = csv.writer(file)     
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['ID','Name','Address','Phone','Courier','Status','Items'])
        for i in range(0,len(orders)):
            writer.writerow(orders[i])

def export_customers():
    # Open database
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="mini-project"
    )
    cursor = db.cursor() # Open cursor
    # Define customers list from DB
    customers = []
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()
    for row in rows:
        customers.append(row)
    cursor.close() # Close cursor
    db.close() # Close DB
    #  Export to customers.csv
    with open('customers.csv', mode='w', newline = '') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['ID','Name','Phone'])
        for i in range(0,len(customers)):
            writer.writerow(customers[i])


# Menus
main_menu_options = ['Exit', 'Products Menu', 'Couriers Menu', 'Orders Menu', 'Customers Menu'] # Main menu options
products_menu_options = ['Main Menu', 'View Products', 'Add Products', 'Edit Products', 'Delete Products', 'Export Products'] # Products menu options
couriers_menu_options = ['Main Menu', 'View Couriers', 'Add Couriers', 'Edit Couriers', 'Delete Couriers', 'Export Couriers'] # Couriers menu options
orders_menu_options = ['Main Menu', 'View Orders', 'Add Orders', 'Update Order Status', 'Edit Orders', 'Delete Orders', 'Export Orders'] # Orders menu options
customers_menu_options = ['Main Menu', 'View Customers', 'Add Customers', 'Edit Customers', 'Delete Customers', 'Export Customers'] # Customers menu options


# App UI
while True:
    
    # Main menu greeting
    print('\nMAIN MENU')
    for count, list in enumerate(main_menu_options):
        print(count, list)
    main_menu = input('\nPlease select an option\n')

    # Main menu option 0 - exit
    if main_menu == '0':
        print('\nGoodbye\n')
        break

    # Main menu option 1 - product menu
    if main_menu == '1':

        # Products menu greeting
        print('\nPRODUCTS MENU')
        for count, list in enumerate(products_menu_options):
            print(count, list)
        products_menu = input('\nPlease select an option\n')
        
        # Products menu option 0 - return to main menu
        if products_menu == '0':
            continue
        
        # Products menu option 1 - print products list
        if products_menu == '1':
            print_products()
            continue

        # Products menu option 2 - add products
        if products_menu == '2':
            add_products()
            print_products()
            continue

        # Products menu option 3 - edit products
        if products_menu == '3':
            edit_products()
            print_products()
            continue

        # Products menu option 4 - delete products
        if products_menu == '4':
            delete_products()
            print_products()
            continue

        # Products menu option 5 - export products
        if products_menu == '5':
            export_products()
            print('\nProducts list exported to products.csv\n')
            continue

        # Products menu else
        else:
            print('\nPlease enter a valid option\n')
            continue

    # Main menu option 2 - couriers menu
    if main_menu == '2':
        
        # Couriers menu greeting
        print('\nCOURIERS MENU')
        for count, list in enumerate(couriers_menu_options):
            print(count, list)
        couriers_menu = input('\nPlease select an option\n')
        
        # Couriers menu option 0 - return to main menu
        if couriers_menu == '0':
            continue
        
        # Couriers menu option 1 - print couriers list
        if couriers_menu == '1':
            print_couriers()
            continue

        # Couriers menu option 2 - add couriers
        if couriers_menu == '2':
            add_couriers()
            print_couriers()
            continue

        # Couriers menu option 3 - edit couriers
        if couriers_menu == '3':
            edit_couriers()
            print_couriers()
            continue

        # Couriers menu option 4 - delete couriers
        if couriers_menu == '4':
            delete_couriers()
            print_couriers()
            continue

        # Couriers menu option 5 - export couriers
        if couriers_menu == '5':
            export_couriers()
            print('\nCouriers list exported to couriers.csv\n')
            continue

        # Couriers menu else
        else:
            print('\nPlease enter a valid option\n')
            continue
    
    # Main menu option 3 - orders menu
    if main_menu == '3':
        
        # Orders menu greeting
        print('\nORDERS MENU')
        for count, list in enumerate(orders_menu_options):
            print(count, list)
        orders_menu = input('\nPlease select an option\n')
        
        # Orders menu option 0 - return to main menu
        if orders_menu == '0':
            continue
        
        # Orders menu option 1 - print orders list
        if orders_menu == '1':
            print_listed_orders()
            continue

        # Orders menu option 2 - add orders
        if orders_menu == '2':
            add_orders()
            print_orders()
            continue

        # Orders menu option 3 - update orders status
        if orders_menu == '3':
            edit_order_status()
            print_orders()
            continue

        # Orders menu option 4 - edit orders
        if orders_menu == '4':
            edit_orders()
            print_orders()
            continue

        # Orders menu option 5 - delete orders
        if orders_menu == '5':
            delete_orders()
            print_orders()
            continue

        # Orders menu option 6 - export orders
        if orders_menu == '6':
            export_orders()
            print('\nOrders list exported to orders.csv\n')
            continue

        # Orders menu else
        else:
            print('\nPlease enter a valid option\n')
            continue
    
    # Main menu option 4 - customers menu
    if main_menu == '4':
        
        # Customers menu greeting
        print('\nCUSTOMERS MENU')
        for count, list in enumerate(customers_menu_options):
            print(count, list)
        customers_menu = input('\nPlease select an option\n')
        
        # Customers menu option 0 - return to main menu
        if customers_menu == '0':
            continue
        
        # Customers menu option 1 - print customers list
        if customers_menu == '1':
            print_customers()
            continue

        # Customers menu option 2 - add customers
        if customers_menu == '2':
            add_customers()
            print_customers()
            continue

        # Customers menu option 3 - edit customers
        if customers_menu == '3':
            edit_customers()
            print_customers()
            continue

        # Customers menu option 4 - delete customers
        if customers_menu == '4':
            delete_customers()
            print_customers()
            continue

        # Customers menu option 5 - export customers
        if customers_menu == '5':
            export_customers()
            print('\nCustomers list exported to customers.csv\n')
            continue

        # Customers menu else
        else:
            print('\nPlease enter a valid option\n')
            continue
 
    # Main menu else
    else:
        print('\nPlease enter a valid option\n')
        continue


















