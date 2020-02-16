import mysql.connector as mysql

db = mysql.connect(host = "localhost", user = "rrajesh0205", passwd = "Longines0205", database = "usertest")

## defining the Query to fetch the user

id =    input("Enter your id       : ")
ui =    input("Enter your username : ")
uipw =  input("Enter your password : ")

add_user = ("INSERT INTO usernew (id, name, code) values('{}', '{}', '{}')".format(id, ui, uipw))

cursor=db.cursor()
cursor.execute(add_user)
db.commit()

print("Updated")
## Closing the cursor and the database

cursor.close()
db.close()
