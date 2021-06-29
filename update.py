import mysql.connector

mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234",
                               host="127.0.0.1", database="hospital",
                               auth_plugin="mysql_native_password")

mycursor = mydb.cursor()

sql = "UPDATE dentists SET dentist_surname = 'Myberg' WHERE dentist_names = 'Godwin'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute('Select * from dentists')
for i in mycursor:
    print(i)
