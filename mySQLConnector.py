import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="rrajesh0205", passwd="Longines0205")
mycursor = mydb.cursor()
mycursor.execute("Show Databases")
for i in mycursor:
    print(i)