## IMPORT PACKAGES
# Import any required packages
import csv


## IMPORT DICTIONARIES
# Import list of products
products = []
with open("products.csv",'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        products.append(row)

# Import list of couriers
couriers = []
with open("couriers.csv",'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        couriers.append(row)

# Import list of orders
orders = []
with open("orders.csv",'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        orders.append(row)


## DEFINE MENU OPTIONS
# Main menu options
main_menu_options = ['Exit', 'Products Menu', 'Couriers Menu', 'Orders Menu']
# Products menu options
products_menu_options = ['Main Menu', 'View Products', 'Add Products', 'Edit Products', 'Delete Products']
# Couriers menu options
couriers_menu_options = ['Main Menu', 'View Couriers', 'Add Couriers', 'Edit Couriers', 'Delete Couriers']
# Orders menu options
orders_menu_options = ['Main Menu', 'View Orders', 'Add Orders', 'Edit Orders', 'Delete Orders']


## WHILE LOOP
# Main menu while loop
while True:

    # Main menu greeting
    for count, list in enumerate(main_menu_options):
        print(count, list)
    main_menu = input(f'MAIN MENU: Please select an option')

    # Main menu option 0 - exit
    if main_menu == '0':
        # Update products.csv
        with open('products.csv', mode='w', newline = '') as file:
            fieldnames = ['products_name', 'products_price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0,len(products)):
                writer.writerow(products[i])
        # Update couriers.csv
        with open('couriers.csv', mode='w', newline = '') as file:
            fieldnames = ['couriers_name', 'couriers_phone']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0,len(couriers)):
                writer.writerow(couriers[i])
        # Update orders.csv
        with open('orders.csv', mode='w', newline = '') as file:
            fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(0,len(orders)):
                writer.writerow(orders[i])
        print('Goodbye')
        break

    # Main menu option 1 - product menu
    if main_menu == '1':

        # Products menu greeting
        for count, list in enumerate(products_menu_options):
            print(count, list)
        products_menu = input(f'PRODUCTS MENU: Please select an option')
        
        # Products menu option 0 - return to main menu
        if products_menu == '0':
            continue
        
        # Products menu option 1 - print products list
        if products_menu == '1':
            for count, list in enumerate(products, 1):
                print(count, list)
            continue

        # Products menu option 2 - add products
        if products_menu == '2':
            # Input products name
            products_name = input('Please enter new product name')
            # Input products name
            products_price = input('Please enter new product price')
            add_products = {'products_name': products_name, 'products_price': products_price}
            products.append(add_products)   
            for count, list in enumerate(products, 1):
                print(count, list)
            continue

        # Products menu option 3 - edit products
        if products_menu == '3':
            for count, list in enumerate(products, 1):
                print(count, list)
            # Delete products
            delete_products = input('Please enter the number of product to delete')
            if 0 < int(delete_products) and int(delete_products) <= len(products):
                del products[int(delete_products)-1]
            else:
                print('Please enter a valid option')
                continue
            # Add products
            # Input products name
            products_name = input('Please enter new product name')
            # Input products name
            products_price = input('Please enter new product price')
            add_products = {'products_name': products_name, 'products_price': products_price}
            products.append(add_products)   
            for count, list in enumerate(products, 1):
                print(count, list)
            continue

        # Products menu option 4 - delete products
        if products_menu == '4':
            for count, list in enumerate(products, 1):
                print(count, list)
            delete_products = input('Please enter the number of product to delete')
            if 0 < int(delete_products) and int(delete_products) <= len(products):
                del products[int(delete_products)-1]
            else:
                print('Please enter a valid option')
                continue
            for count, list in enumerate(products, 1):
                print(count, list)
            continue

        # Products menu else
        else:
            print('Please enter a valid option')
            continue

    # Main menu option 2 - couriers menu
    if main_menu == '2':
        
        # Couriers menu greeting
        for count, list in enumerate(couriers_menu_options):
            print(count, list)
        couriers_menu = input(f'COURIERS MENU: Please select an option')
        
        # Couriers menu option 0 - return to main menu
        if couriers_menu == '0':
            continue
        
        # Couriers menu option 1 - print couriers list
        if couriers_menu == '1':
            for count, list in enumerate(couriers, 1):
                print(count, list)
            continue

        # Couriers menu option 2 - add couriers
        if couriers_menu == '2':
            # Input couriers name
            couriers_name = input('Please enter new courier name')
            # Input couriers name
            couriers_phone = input('Please enter new courier number')
            add_couriers = {'couriers_name': couriers_name, 'couriers_phone': couriers_phone}
            couriers.append(add_couriers)   
            for count, list in enumerate(couriers, 1):
                print(count, list)
            continue

        # Couriers menu option 3 - edit couriers
        if couriers_menu == '3':
            for count, list in enumerate(couriers, 1):
                print(count, list)
            # Delete couriers
            delete_couriers = input('Please enter the number of courier to edit')
            if 0 < int(delete_couriers) and int(delete_couriers) <= len(couriers):
                del couriers[int(delete_couriers)-1]
            else:
                print('Please enter a valid option')
                continue
            # Add couriers
            # Input couriers name
            couriers_name = input('Please enter new courier name')
            # Input couriers name
            couriers_phone = input('Please enter new courier number')
            add_couriers = {'couriers_name': couriers_name, 'couriers_phone': couriers_phone}
            couriers.append(add_couriers)   
            for count, list in enumerate(couriers, 1):
                print(count, list)
            continue

        # Couriers menu option 4 - delete couriers
        if couriers_menu == '4':
            for count, list in enumerate(couriers, 1):
                print(count, list)
            delete_couriers = input('Please enter the number of courier to delete')
            if 0 < int(delete_couriers) and int(delete_couriers) <= len(couriers):
                del couriers[int(delete_couriers)-1]
            else:
                print('Please enter a valid option')
                continue
            for count, list in enumerate(couriers, 1):
                print(count, list)
            continue

        # Couriers menu else
        else:
            print('Please enter a valid option')
            continue
    
    # Main menu option 3 - orders menu
    if main_menu == '3':
        
        # Orders menu greeting
        for count, list in enumerate(orders_menu_options):
            print(count, list)
        orders_menu = input(f'ORDERS MENU: Please select an option')
        
        # Orders menu option 0 - return to main menu
        if orders_menu == '0':
            continue
        
        # Orders menu option 1 - print orders list
        if orders_menu == '1':
            for count, list in enumerate(orders, 1):
                print(count, list)
            continue

        # Orders menu option 2 - add orders
        if orders_menu == '2':
            # Input customer name
            customer_name = input('Please enter customer name')
            # Input customer address
            customer_address = input('Please enter customer address')
            # Input customer phone number
            customer_phone = input('Please enter customer phone number')
            # Select courier
            for count, list in enumerate(couriers, 1):
                print(count, list)
            select_courier = input('Please enter a number to select courier')
            select_courier = couriers[int(select_courier)-1]
            # Set order status
            status = "preparing"
            add_orders = {'customer_name': customer_name, 'customer_address': customer_address, 'customer_phone': customer_phone, 'courier': select_courier, 'status': status}
            orders.append(add_orders)
            for count, list in enumerate(orders, 1):
                print(count, list)
            continue

        # Orders menu option 3 - edit orders
        if orders_menu == '3':
            for count, list in enumerate(orders, 1):
                print(count, list)
            # Delete orders
            delete_orders = input('Please enter the number of order to edit')
            if 0 < int(delete_orders) and int(delete_orders) <= len(orders):
                del orders[int(delete_orders)-1]
            else:
                print('Please enter a valid option')
                continue
            # Add orders
            # Input customer name
            customer_name = input('Please enter customer name')
            # Input customer address
            customer_address = input('Please enter customer address')
            # Input customer phone number
            customer_phone = input('Please enter customer phone number')
            # Select courier
            for count, list in enumerate(couriers, 1):
                print(count, list)
            select_courier = input('Please enter a number to select courier')
            select_courier = couriers[int(select_courier)-1]
            # Set orders status
            status = "preparing"
            add_orders = {'customer_name': customer_name, 'customer_address': customer_address, 'customer_phone': customer_phone, 'courier': select_courier, 'status': status}
            orders.append(add_orders)
            for count, list in enumerate(orders, 1):
                print(count, list)
            continue

        # Orders menu option 4 - delete orders
        if orders_menu == '4':
            for count, list in enumerate(orders, 1):
                print(count, list)
            delete_orders = input('Please enter the number of order to delete')
            if 0 < int(delete_orders) and int(delete_orders) <= len(orders):
                del orders[int(delete_orders)-1]
            else:
                print('Please enter a valid option')
                continue
            for count, list in enumerate(orders, 1):
                print(count, list)
            continue
        
        # Orders menu else
        else:
            print('Please enter a valid option')
            continue
    

    # Main menu else
    else:
        print('Please enter a valid option')
        continue


