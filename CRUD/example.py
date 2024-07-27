import mysql.connector

# Database connection details 
mydb = mysql.connection.connect(
    host='localhost',
    user='root',
    passwd='87628762'
    database='johnitopa'
)

mycursor = mysql.cursor()

# create a table named `customer` (if it doest not exist)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
)
""")

print("Table created successfully!")

# Insert some customer data
