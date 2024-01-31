import mysql.connector

dataBase=mysql.connector.connect(
    host= 'localhost',
    user='root',
    password ='1234',

)

#prepare a cursor object
cursorObject=dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE finetechco")

print("All Done!")