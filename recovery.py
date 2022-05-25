## Creat dictionaries (in case data is wiped)
import csv

# Products
with open('products.csv', mode='w', newline = '') as file:
    fieldnames = ['id', 'name', 'price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "id": 1,
        "name": "Tea",
        "price": 2
    })
    writer.writerow({
        "id": 2,
        "name": "Coffee",
        "price": 3
    })
    writer.writerow({
        "id": 3,
        "name": "Water",
        "price": 1
    })
    writer.writerow({
        "id": 4,
        "name": "Orange Juice",
        "price": 2.5
    })
    writer.writerow({
        "id": 5,
        "name": "Coke",
        "price": 1.5
    })
    writer.writerow({
        "id": 6,
        "name": "Lemonade",
        "price": 1.5
    })


# Couriers
with open('couriers.csv', mode='w', newline = '') as file:
    fieldnames = ['id', 'name', 'phone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "id": 1,
        "name": "Albert",
        "phone": "0789887881"
    })
    writer.writerow({
        "id": 2,
        "name": "Beatrice",
        "phone": "0789887882"
    })
    writer.writerow({
        "id": 3,
        "name": "Charlie",
        "phone": "0789887883"
    })
    writer.writerow({
        "id": 4,
        "name": "David",
        "phone": "0789887884"
    })
    writer.writerow({
        "id": 5,
        "name": "Eunice",
        "phone": "0789887885"
    })
    writer.writerow({
        "id": 6,
        "name": "Felicity",
        "phone": "0789887886"
    })




# Orders
with open('orders.csv', mode='w', newline = '') as file:
    fieldnames = ['id', 'name', 'address', 'phone', 'courier', 'status', 'items']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "id": 1,
        "name": "John",
        "address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "phone": "0789887334",
        "courier": 2,
        "status": "preparing",
        "items": "1, 3, 4"
    })
    writer.writerow({
        "id": 2,
        "name": "Jane",
        "address": "Unit 3, 57 Left Street, LONDON, E3 2BC",
        "phone": "07895839273",
        "courier": 5,
        "status": "preparing",
        "items": "2, 6"
    })
    writer.writerow({
        "id": 3,
        "name": "Jeremy",
        "address": "Unit 7, 39 Right Street, LONDON, SE5 4JK",
        "phone": "07573950347",
        "courier": 1,
        "status": "preparing",
        "items": "5"
    })
    writer.writerow({
        "id": 4,
        "name": "Janice",
        "address": "Unit 12, 84 Down Street, LONDON, NW2 9GO",
        "phone": "07576910334",
        "courier": 4,
        "status": "preparing",
        "items": "1, 2, 3, 6"
    })



# Customers
with open('customers.csv', mode='w', newline = '') as file:
    fieldnames = ['id', 'name', 'phone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "id": 1,
        "name": "Hardik",
        "phone": "07756293011"
    })
    writer.writerow({
        "id": 2,
        "name": "Marshall",
        "phone": "07756293012"
    })
    writer.writerow({
        "id": 3,
        "name": "Hardik Marshall",
        "phone": "07756293013"
    })
    writer.writerow({
        "id": 4,
        "name": "Marshall Hardik",
        "phone": "07756293014"
    })

