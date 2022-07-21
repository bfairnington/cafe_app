# readme

Setup a Docker container to run a local MySQL database.
Ensure the adminer container is running.

app.py uses the following login details as default:
        host="localhost",
        user="root",
        password="password",
        database="mini-project"

In the database create the following tables if they do not exist:
- products
- couriers
- orders
- customers

The schema for each of these tables can be found in .csv files in this repo

Run app.py

