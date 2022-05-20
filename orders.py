## Creat Orders File (in case data is wiped)
import csv

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
