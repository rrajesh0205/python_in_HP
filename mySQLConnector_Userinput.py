import mysql.connector as mysql

db = mysql.connect(host = "localhost", user = "rrajesh0205", passwd = "Longines0205", database = "usertest")

## defining the Query to fetch the user

id =    input("Enter your id       : ")
ui =    input("Enter your username : ")
uipw =  input("Enter your password : ")

query = "SELECT name FROM usernew where id =%s"
id = (1,)
cursor = db.cursor()
cursor.execute(query, id)
record = cursor.fetchone()

query = "SELECT code FROM usernew where id =%s"
id = (1,)
cursor = db.cursor()
cursor.execute(query, id)
record1 = cursor.fetchone()

## Assigning the fetched data to the User Input data

ui = record[0]
uipw = record1[0]

if ui == record[0] and uipw == record1[0]:
    print("Hi!", ui, ", There is a user in the same name.")
else:
    print("Hi!", ui, ", Record has been updated")
    print("New user created and Updated")

db.commit()


## Closing the cursor and the database

cursor.close()
db.close()
