import mysql.connector

"""sd=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')

cursor=sd.cursor()


sql='SELECT * FROM EMPLOYEE'


cursor.execute(sql)

result=cursor.fetchmany(size=3)
print(result)

sd.close()"""



#Example from me.

"""m_s_d=mysql.connector.connect(user='root',
                              passwd='root',
                              host='localhost',
                              database='mydatabase')


cursor=m_s_d.cursor()

c_sql='SELECT * FROM INFO'

cursor.execute(c_sql)

#The next line is retrieveing first row data from table INFO
result=cursor.fetchone()
print(result)

#The next line is retrieveing brings two rows data from table INFO
result=cursor.fetchmany(size=2)
print(result)
#The next line is retrieveing all rows data from table INFO
result=cursor.fetchall()
print(result)

m_s_d.close()"""




#WHERE CLAOSE.
"""w_c=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')

cursor=w_c.cursor()

cursor.execute('DROP TABLE IF EXISTS EMPLOYYES')
sql='''CREATE TABLE EMPLOYYES(FIRST_NAME CHAR(20) NOT NULL,
                              LAST_NAME CHAR(20),
                              AGE INT,
                              SEX CHAR(1),
                              INCOME FLOAT
)'''

cursor.execute(sql)

insert_stmt='''INSERT INTO EMPLOYYES(FIRST_NAME,
                                     LAST_NAME,
                                     AGE,
                                     SEX,
                                     INCOME)
                                     VALUE('Raj','Kandukur',20,'M',7000),
                                          ('Krishna','Sharma',19,'M',2000),
                                          ('Ramya','Ramapriya',25,'F',5000),
                                          ('Mac','Mohan',26,'M',2000)'''
cursor.execute(insert_stmt)
w_c.commit()

cursor.execute('SELECT * FROM EMPLOYYES WHERE AGE <23')
print(cursor.fetchall())


w_c.close()"""

#Example from me.

"""me_wc=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydatabase')



cursor=me_wc.cursor()

cursor.execute('DROP TABLE IF EXISTS information')

sql='''CREATE TABLE information(FIRST_NAME CHAR(15) NOT NULL,
                                LAST_NAME CHAR(15),
                                AGE INT,
                                INCOME FLOAT)'''

cursor.execute(sql)

insrt_stmt='''INSERT INTO information(FIRST_NAME,LAST_NAME,AGE,INCOME)
                                VALUE('Abdulrahman','Ahmed',21,8000)
                                     ,('Ahmed','Ali',22,9000)
                                     ,('Jaber','Ahmed',35,14000)
                                     ,('AZAY','AL ASABY',45,100000)'''

cursor.execute(insrt_stmt)
me_wc.commit()


#NOW retrieving specific records using the where clause.
cursor.execute('SELECT * FROM information WHERE INCOME >0')

print(cursor.fetchall())
me_wc.close()"""
