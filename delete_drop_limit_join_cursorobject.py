import mysql.connector

"""
delete=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')


cursor=delete.cursor()

print('Contents of the table:')
cursor.execute('SELECT * from EMPLOYEE')
print(cursor.fetchall())


sql='''DELETE FROM EMPLOYEE WHERE AGE > '%d' '''% (25)

try:
    cursor.execute(sql)
    delete.commit()

except:
    delete.rollback()

print("Contents of the table after delete operation ")
cursor.execute("SELECT * FROM EMPLOYEE")
print(cursor.fetchall())

delete.close()"""



#EXMAPLE FROM ME 
"""
me_delete=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydatabase')




cursor=me_delete.cursor()


print("Contents of the table: ")
cursor.execute("SELECT * FROM information")
print(cursor.fetchall())


my_command="DELETE FROM information WHERE INCOME > '%d' " % (10000)
#Note the query above if you see '%d' % (10000) when program run is do rplace.
#THE query above is delete if ICOME greate then 10000.

try:

    cursor.execute(my_command)
    me_delete.commit()


except:

    me_delete.rollback()


print('Contents of the table after delete operation')

cursor.execute("SELECT * FROM information")

print(cursor.fetchall())"""




#Drop table 
"""

drop=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')



cursor=drop.cursor()

cursor.execute("SHOW TABLES") 
print(cursor.fetchall())

cursor.execute("DROP TABLE IF EXISTS INFO")

print("Table dropped...")

cursor.execute("SHOW TABLES")
print(cursor.fetchall())
drop.close()"""


#EMAPLE FROM ME.

"""
me_drop=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydatabase')


cursor=me_drop.cursor()


cursor.execute("SHOW TABLES")
print(cursor.fetchall())


#cursor.execute("DROP TABLE information")
cursor.execute("DROP TABLE IF EXISTS INFORMATION")
print('Table is dropped')

cursor.execute("SHOW TABLES")
print(cursor.fetchall())

me_drop.close()"""


#LIMITE
"""
limit=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')


cursor=limit.cursor()


cursor.execute("SELECT * FROM EMPLOYEE LIMIT 2")
print(cursor.fetchall())
#Note if see LIMIT 2 that is mean give me the first and seconed records.

limit.close()"""


#EMAPLE FROM ME.
"""me_limit=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')


cursor=me_limit.cursor()


#cursor.execute("SELECT * FROM EMPLOYEE LIMIT 6")
cursor.execute("SELECT * from EMPLOYEE LIMIT 2 OFFSET 2")
print(cursor.fetchall())
#Note if see LIMIT 2 that is mean give me the first and seconed records.
#OFFSET 2: This tells the database to skip the first 2 rows in the result set and start returning rows from the third row onward.
me_limit.close()"""

#JOIN

join=mysql.connector.connect(user='root',passwd='root',host='localhost',database='mydb')



cursor=join.cursor()

sql = '''SELECT * from EMPLOYEE1 INNER JOIN CONTACT ON EMPLOYEE1.contact = CONTACT.ID'''
cursor.execute(sql)

result=cursor.fetchall()
print(result)
join.close()


