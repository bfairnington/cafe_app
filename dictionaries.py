## Creat dictionaries (in case data is wiped)
import csv

# Products
with open('products.csv', mode='w', newline = '') as file:
    fieldnames = ['products_name', 'products_price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "products_name": "Tea",
        "products_price": 2
    })
    writer.writerow({
        "products_name": "Coffee",
        "products_price": 3
    })
    writer.writerow({
        "products_name": "Water",
        "products_price": 1
    })
    writer.writerow({
        "products_name": "Orange Juice",
        "products_price": 2.5
    })
    writer.writerow({
        "products_name": "Coke",
        "products_price": 1.5
    })
    writer.writerow({
        "products_name": "Lemonade",
        "products_price": 1.5
    })


# Couriers
with open('couriers.csv', mode='w', newline = '') as file:
    fieldnames = ['couriers_name', 'couriers_phone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "couriers_name": "Albert",
        "couriers_phone": "0789887881"
    })
    writer.writerow({
        "couriers_name": "Beatrice",
        "couriers_phone": "0789887882"
    })
    writer.writerow({
        "couriers_name": "Charlie",
        "couriers_phone": "0789887883"
    })
    writer.writerow({
        "couriers_name": "David",
        "couriers_phone": "0789887884"
    })
    writer.writerow({
        "couriers_name": "Eunice",
        "couriers_phone": "0789887885"
    })
    writer.writerow({
        "couriers_name": "Felicity",
        "couriers_phone": "0789887886"
    })




# Orders
with open('orders.csv', mode='w', newline = '') as file:
    fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "courier": "Beatrice",
        "status": "preparing"
    })
    writer.writerow({
        "customer_name": "Jane",
        "customer_address": "Unit 3, 57 Left Street, LONDON, E3 2BC",
        "customer_phone": "07895839273",
        "courier": "Eunice",
        "status": "preparing"
    })
    writer.writerow({
        "customer_name": "Jeremy",
        "customer_address": "Unit 7, 39 Right Street, LONDON, SE5 4JK",
        "customer_phone": "07573950347",
        "courier": "Albert",
        "status": "preparing"
    })
    writer.writerow({
        "customer_name": "Janice",
        "customer_address": "Unit 12, 84 Down Street, LONDON, NW2 9GO",
        "customer_phone": "07576910334",
        "courier": "David",
        "status": "preparing"
    })
