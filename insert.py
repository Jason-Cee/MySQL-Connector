import mysql.connector

mydb = mysql.connector.connect(user="lifechoices",
                               password="@Lifechoices1234",
                               host="127.0.0.1", database="hospital",
                               auth_plugin="mysql_native_password")

mycursor = mydb.cursor()

sql = "INSERT INTO dentists  VALUES (%s, %s, %s, %s, %s)"
val = ("GDP", "Godwin", "Dr Dzvapatsva", "0735887757", "1023450")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute('Select * from dentists')
for i in mycursor:
    print(i)
