import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="supriya@123"
)

#mycurs = mydb.cursor()
#mycurs.execute("SHOW DATABASES")

#for db in mycurs:
 #   print(db)