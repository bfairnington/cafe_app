## IMPORT PACKAGES
# Import any required packages
import csv


## IMPORT LISTS
# Import list of products
products = []
file = open('products.txt','r')
for line in file.readlines():
    products.append(line.strip())

# Import list of couriers
couriers = []
file = open('couriers.txt','r')
for line in file.readlines():
    couriers.append(line.strip())

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
        # Update products.txt
        with open('products.txt', 'w') as file:
            for count, value in enumerate(products):
                file.writelines(value + '\n')
        # Update couriers.txt
        with open('couriers.txt', 'w') as file:
            for count, value in enumerate(couriers):
                file.writelines(value + '\n')
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
            print(products)
            continue

        # Products menu option 2 - add products
        if products_menu == '2':
            add_products = input('Please enter new product name')
            products.append(add_products)
            print(products)
            continue

        # Products menu option 3 - edit products
        if products_menu == '3':
            delete_products = input('Please enter name of product to edit')
            if delete_products in products:
                products.remove(delete_products)
            else:
                print('Please enter a valid option')
                continue
            add_products = input('Please enter the new name of product')
            products.append(add_products)       
            print(products)
            continue

        # Products menu option 4 - delete products
        if products_menu == '4':
            delete_products = input('Please enter name of product to delete')
            if delete_products in products:
                products.remove(delete_products)
            else:
                print('Please enter a valid option')
                continue
            print(products)
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
            print(couriers)
            continue

        # Couriers menu option 2 - add couriers
        if couriers_menu == '2':
            add_couriers = input('Please enter new courier name')
            couriers.append(add_couriers)
            print(couriers)
            continue

        # Couriers menu option 3 - edit couriers
        if couriers_menu == '3':
            delete_couriers = input('Please enter name of courier to edit')
            if delete_couriers in couriers:
                couriers.remove(delete_couriers)
            else:
                print('Please enter a valid option')
                continue
            add_couriers = input('Please enter the new name of courier')
            couriers.append(add_couriers)       
            print(couriers)
            continue

        # Couriers menu option 4 - delete couriers
        if couriers_menu == '4':
            delete_couriers = input('Please enter name of courier to delete')
            if delete_couriers in couriers:
                couriers.remove(delete_couriers)
            else:
                print('Please enter a valid option')
                continue
            print(couriers)
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
            # Delete order
            delete_orders = input('Please enter the number of order to edit')
            if 0 < int(delete_orders) and int(delete_orders) <= len(orders):
                del orders[int(delete_orders)-1]
            else:
                print('Please enter a valid option')
                continue
            # Add order
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





