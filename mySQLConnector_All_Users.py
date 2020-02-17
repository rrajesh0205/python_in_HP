import mysql.connector as mysql

db = mysql.connect(host = "localhost", user = "rrajesh0205", passwd = "Longines0205", database = "usertest")

## defining the Query to fetch the user

query = "SELECT name FROM usernew where name =%s"
name = input("Enter the name...")
cursor = db.cursor()
cursor.execute(query, (name,))
record = cursor.fetchone()

## Assigning the fetched data to the User Input data

ui = str(record[0])

## Getting the user input and cross checking with the database

print('Please Enter correct your username and password to Login')
count = 1
while count < 4:
    ui =    input("Enter your username : ")
    uipw =  input("Enter your password : ")
    if record[0] == ui:
        print("Hi!", ui,", You have been logged in.")
        count = 5
    else:
        print("Hi!", ui,", The credentials entered are not matching in our records.")
        if count == 3:
            print("Hi!", ui,", You have exceeded the maximum number of attempts.")
            print("Hi!", ui, ", Maybe you are a new user, want to create a new user")

        count += 1


## Closing the cursor and the database

cursor.close()
db.close()
