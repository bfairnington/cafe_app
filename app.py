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


# Main menu options
main_menu_options = {
    0 : 'Exit',
    1 : 'Products Menu',
    2 : 'Couriers Menu'
    }

# Products menu options
products_menu_options = {
    0 : 'Main Menu',
    1 : 'View Products',
    2 : 'Add Products',
    3 : 'Edit Products',
    4 : 'Delete Products'
    }

# Couriers menu options
couriers_menu_options = {
    0 : 'Main Menu',
    1 : 'View Couriers',
    2 : 'Add Couriers',
    3 : 'Edit Couriers',
    4 : 'Delete Couriers'
    }


# Main menu while loop
while True:

    # Main menu greeting
    main_menu = input(f'MAIN MENU: Please select from the following options: {main_menu_options}')
    
    # Main menu option 0 - exit
    if main_menu == '0':
        with open('products.txt', 'w') as file:
            for count, value in enumerate(products):
                file.writelines(value + '\n')
        with open('couriers.txt', 'w') as file:
            for count, value in enumerate(couriers):
                file.writelines(value + '\n')
        print('Goodbye')
        break

    # Main menu option 1 - product menu
    if main_menu == '1':

        # Products menu greeting
        products_menu = input(f'PRODUCT MENU: Please select from the following options: {products_menu_options}')
        
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
            products.remove(delete_products)
            print(products)
            continue

        # Products menu else
        else:
            print('Please enter a valid option')
            continue

    # Main menu option 2 - couriers menu
    if main_menu == '2':
        
        # Couriers menu greeting
        couriers_menu = input(f'COUREIR MENU: Please select from the following options: {couriers_menu_options}')
        
        # Couriers menu option 0 - return to main menu
        if couriers_menu == '0':
            continue
        
        # Couriers menu option 1 - print couriers list
        if couriers_menu == '1':
            print(couriers)
            continue

        # Couriers menu option 2 - add couriers
        if couriers_menu == '2':
            add_couriers = input('Please enter new product name')
            couriers.append(add_couriers)
            print(couriers)
            continue

        # Couriers menu option 3 - edit couriers
        if couriers_menu == '3':
            delete_couriers = input('Please enter name of product to edit')
            if delete_couriers in couriers:
                products.remove(delete_couriers)
            else:
                print('Please enter a valid option')
                continue
            add_couriers = input('Please enter the new name of product')
            couriers.append(add_couriers)       
            print(couriers)
            continue

        # Couriers menu option 4 - delete couriers
        if couriers_menu == '4':
            delete_couriers = input('Please enter name of product to delete')
            if delete_couriers in couriers:
                products.remove(delete_couriers)
            else:
                print('Please enter a valid option')
                continue
            print(couriers)
            continue
        
        # Couriers menu else
        else:
            print('Please enter a valid option')
            continue
    
    # Main menu else
    else:
        print('Please enter a valid option')
        continue

