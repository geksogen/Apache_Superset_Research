import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ANSKk08aPEDbFjDO"
)

# Create a database
cursor = connection.cursor()
cursor.execute("CREATE DATABASE website_traffic")