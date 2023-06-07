import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS crmapp")

print("Database created successfully")
