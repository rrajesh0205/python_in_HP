import mysql.connector as mysql

db = mysql.connect(host = "localhost", user = "rrajesh0205", passwd = "Longines0205", database = "usertest")

## defining the Query to fetch the user

query = "SELECT name FROM usernew where id =%s"
id = (1,)
cursor = db.cursor()
cursor.execute(query, id)
record = cursor.fetchone()

## defining the Query to fetch the password

query = "SELECT code FROM usernew where id =%s"
id = (1,)
cursor = db.cursor()
cursor.execute(query, id)
record1 = cursor.fetchone()


## Assigning the fetched data to the User Input data

user_name = record[0]
uipw = record1[0]

## Getting the user input and cross checking with the database

print('Please Enter correct your username and password to Login')
count = 1
while count < 4:
    ui =    input("Enter your username : ")
    uipw =  input("Enter your password : ")
    if ui == record[0] and uipw == record1[0]:
        print("Hi!", ui,", You have been logged in.")
        count = 5
    else:
        print("Hi!", ui,", The credentials entered are not matching in our records.")
        if count == 3:
            print("Hi!", ui,", You have exceeded the maximum number of attempts.")
        count += 1

## Closing the cursor and the database

cursor.close()
db.close()
