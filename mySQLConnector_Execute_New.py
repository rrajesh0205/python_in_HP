import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="rrajesh0205", passwd="Longines0205", database="PSCBSE")
mycursor = mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
    print(i)
