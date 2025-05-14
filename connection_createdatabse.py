import mysql.connector




#Connection database from MySQL Server
"""connection=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')

cursor=connection.cursor()

cursor.execute("SELECT DATABASE()")

rs=cursor.fetchone()
print(rs)"""



#Create database from mysql using python
"""connection=mysql.connector.connect(user='root',passwd='root',host='localhost')

cursor=connection.cursor()

drop="DROP database IF EXISTS abdulrahman"

sql="CREATE DATABASE SR7"

cursor.execute(drop)



print()
print('The list of databases')
cursor.execute("SHOW DATABASES")
result=cursor.fetchall()

for row in result:
    print(row)

cursor.close()
connection.close()
"""

"""connection=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')

cursor=connection.cursor()

cursor.execute("SELECT DATABASE()")

rs=cursor.fetchone()
print(rs)"""