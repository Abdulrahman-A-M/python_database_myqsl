import mysql.connector
###Create Table.
"""#establishing connection.
conn_server=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')

#Creatign a cusor.
cursor=conn_server.cursor()

#Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement.

sql='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''

cursor.execute(sql)



#Closing the connection.

conn_server.close()"""

#Exmaple from me.
"""cs=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydatabase')

cusor=cs.cursor()

cusor.execute("DROP TABLE IF EXISTS INFO")

sql='''CREATE TABLE INFO(
        FIRST_NAME CHAR(10) NOT NULL,
        LAST_NAME CHAR(10),
        AGE INT,
        SEX CHAR(5),
        INCOME FLOAT
)'''

cusor.execute(sql)


cs.close()
"""

#Insert Data.
conn=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')

cusor=conn.cursor()

sql=('INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)''VALUES (%s, %s, %s, %s, %s)' )

data=('Ammer','Ahmed',36,'M',10000)

try:
    cusor.execute(sql,data)


    conn.commit()
    print('yes')
except :

    conn.rollback()
    print('nooo')

print('Data inserted')
conn.close()

#Example from me .
"""con_ser=mysql.connector.connect(user='root',
                                passwd='root',
                                host='localhost',
                                database='mydatabase'
  )


cusor=con_ser.cursor()

sql='''INSERT INTO INFO(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
       VALUE('Ahmed','Ali',24,'M',9000)'''

#You can use the way instead above
'''insert=(
'INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)'
'VALUES (%s, %s, %s, %s, %s)' )
data=('Abdulrahma','Ahmed',23,'M',10000)

'''


try:

    cusor.execute(sql)

    con_ser.commit()
    print('The data inserted')
except:

    con_ser.rollback()
    print('noo')


con_ser.close()"""




