import mysql.connector

"""mysimp=mysql.connector.connect(user='root',passwd='root',host='localhost',database='simple_project')


#Create cursor.
cursor=mysimp.cursor()


command_sql='''CREATE TABLE information(
            FIRST_NAME CHAR(15),
             LAST_NAME CHAR(15),
             AGE INT,
             FROM_CITY CHAR(10),
             MAJOR CHAR(15)
)'''

cursor.execute(command_sql)

cursor.close()

mysimp.close()"""

#NOW INSERT THE TABLE.

"""cursor=mysimp.cursor()

inser_sql='''INSERT INTO information(FIRST_NAME,LAST_NAME,AGE,FROM_CITY,MAJOR)
              VALUE('Abdulrahman','Ahmed',22,'Asser','Cyber security')'''


try:
   
    cursor.execute(inser_sql)
    mysimp.commit()
    print('The data is insert into table is do.')
    
except:

     mysimp.rollback()
     print('The data is not inser into table!')"""
     
#THIS PROJECT IS FOR EXISRIESED ABOUT WHAT YOU LEARNED.

"""simple=mysql.connector.connect(user='root',passwd='root',host='localhost',database='SIMPLE_PROJECT_2')

cursor=simple.cursor()

sql='''CREATE TABLE PERSONAL_IDENTITY(FULL_NAME CHAR(40)NOT NULL,
                                    ID_NUMBER_PERSONAL INT,
                                    DATE_OF_BIRTH INT
)'''

conmmand_insert='''INSERT INTO PERSONAL_IDENTITY
(FULL_NAME,ID_NUMBER_PERSONAL,DATE_OF_BIRTH)
VALUE('Abdulrahman Ahmed Muhammed',22,2003),
      ('Ahmed',33,1999)'''




try:

    cursor.execute(sql)
    print('THE TABLE DONE')
    
    cursor.execute(conmmand_insert)
    simple.commit()
    print('THE INSERT IS DONE')

    cursor.execute('SELECT * FROM PERSONAL_IDENTITY WHERE ID_NUMBER_PERSONAL>30 ')

    result=cursor.fetchall()
    print(result)

except:
    cursor.execute('DROP TABLE IF EXISTS PERSONAL_IDENTITY')
    print('The operation is not runing.')


simple.close()"""



