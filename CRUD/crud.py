import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='87628762',
    database='johnitopa'
)

mycursor = mydb.cursor()

# Insert some empl

mycursor.execute("")
for i in mycursor:
    print(i)

# Closing connection
mycursor.close()
mydb.close()