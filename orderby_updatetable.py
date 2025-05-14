import mysql.connector

"""#establishing the connection
conn = mysql.connector.connect(
   user='root', password='root', host='localhost', database='mydb')

#Creating a cursor object using the cursor() method.
cursor=conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

sql='''CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,
                            LAST_NAME CHAR(20),
                            AGE INT,
                            SEX CHAR(1),
                            INCOME FLOAT
)'''

cursor.execute(sql)

#Populating the table.
insert_stmt = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES(%s, %s, %s, %s, %s)"

data=[ ('Krishna','Sharma',26,'M',2000),
      ('Raj','Kandukuri',20,'M',7000),
      ('Ramya','Ramapriya',25,'F',5000),
      ('Mac','Mohan',26,'M',2000)]

cursor.executemany(insert_stmt,data)
conn.commit()

#Retrieving sepcific records using the ORDER BY clause.

cursor.execute('SELECT * FROM EMPLOYEE ORDER BY AGE DESC')
print(cursor.fetchall())

#Closing the connection.
conn.close()"""

#Update Table.
"""update_table=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')


cursor=update_table.cursor()


sql='''UPDATE EMPLOYEE SET AGE=AGE+2 WHERE AGE'''


try:
    
    cursor.execute(sql)
    update_table.commit()


except:
    
    update_table.rollback


cursor.execute("SELECT * FROM EMPLOYEE")

print(cursor.fetchall())

update_table.close"""
#Exmaple from me.

me_update_table=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydatabase')

cursor=me_update_table.cursor()

sqls='''UPDATE information SET INCOME=INCOME+100 WHERE INCOME'''

sql='''SELECT * FROM information'''


try:
    cursor.execute(sqls)
    me_update_table.commit()

except:
     
     me_update_table.rollback


cursor.execute(sql)

print(cursor.fetchall())

me_update_table.close()


