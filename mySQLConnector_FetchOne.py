import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="rrajesh0205", passwd="Longines0205", database="DBMHSS")
mycursor = mydb.cursor()
mycursor.execute("select * from student")
result = mycursor.fetchone()

for i in result:
    print(i)
