import mysql.connector as mysql

try:

    connection = mysql.connect(
    host = "localhost",
    user = "rrajesh0205",
    passwd = "Longines0205",
    database = "usertest"
    )

    ## defining the Query
    query = "SELECT name FROM usernew where id =%s"
    id = (1,)
    cursor = connection.cursor()
    cursor.execute(query, id)
    record = cursor.fetchone()

    query = "SELECT code FROM usernew where id =%s"
    id = (1,)
    cursor = connection.cursor()
    cursor.execute(query, id)
    record1 = cursor.fetchone()


## Assigning the fetched data to the User Input data
    user_name = record[0]
    uipw = record1[0]

    print('Please Enter correct your username and password to Login')
    count = 0
    while count < 3:
        ui =    input("Enter your username : ")
        uipw =  input("Enter your password : ")
        if ui == record[0] and uipw == record1[0]:
            print("Hi", ui, "You have been logged to")
            count =5
        else:
            print("Hi", ui, "The credentials entered are not matching in our records.")
            count += 1

except mysql.connector.Error as error:
    print("Failed to get record from the database: {}".format(error))

finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")





