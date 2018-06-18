#1
'''
Done using mysql
'''
#2
import pymysql as pm
try:
     con = pm.connect(host='localhost', database='myDB1', user='vanshika')

     cursor = con.cursor()

     query = "insert into books(bookID, titleID, genre, location) \
     values(%s, %s, %s, %s)"

     records = [(112, 't1', 'drama', 'India'),
                (24, 't2', 'romance', 'UK'),
                (32, 't3', 'thriller', 'Korea')]

     cursor.executemany(query, records)
     
     
      query = "insert into Titles(titleID, title, ISBN, publisherID, puclicationYear) \
     values(%s, %s, %s, %s, %s)"

     records = [('t1', 'XYZ', 1234543567890,789,2016),
                ('t2', 'ABC', 0987654321111,456,2000),
                ('t3', 'QWE', 7410852963456,123,2012)]

     cursor.executemany(query, records)
     
     query = "insert into publishers(publisherID, Name,streetAddress,suiteNUmber,ZIPcodeID) \
     values(%s, %s, %s, %s,%s)"

     records = [(123, 'qaz', 'address1',177, 1),
                (789, 'wsx', 'address2',54, 2),
                (456, 'edc', 'address3', 254,3)]
     

     cursor.executemany(query, records)
     con.commit()
     
      query = "insert into ZIPCodes(ZIPcodeID, city, state,ZIPCode) \
     values(%s, %s, %s, %s)"

     records = [(1, 'A', 'state1', 234241),
                (2, 'B', 'state2',542344),
                (3, 'C', 'state3', 254876)]
     cursor.executemany(query, records)
     con.commit()     

     
     query = "insert into AuthorTitles(TitleID, AuthorID, AuthorTitleID) \
     values(%s, %s, %s, %s)"

     records = [('t2', 'A1', 'AT1'),
                ('t3', 'A2', 'AT34'),
                ('t1', 'A3', 'AT76')]
     

     cursor.executemany(query, records)
     con.commit()


      query = "insert into Authors(AuthorID, FName,MName,LName) \
     values(%s, %s, %s, %s)"

     records = [('A3', 'Chetan', 'Kumar','Bhagat'),
                ('A1', 'Durjoy', 'Singh','Datta'),
                ('A2', 'Joanne', 'Katheline', 'Rowling')]     

     cursor.executemany(query, records)
     con.commit()

except pm.DatabaseError as e:
     if con:
         con.rollback()
         print('Problem occured: ', e)

finally:
     if cursor:
         cursor.close()
     if con:
         con.close()
     print('Done!!')
     
#3
try:
    con = pm.connect(host='localhost', database='myDB1', user='vanshika')

    cursor = con.cursor()

    query = "update Authors set Mname='K.' where AuthorID= 'A2'"
    cursor.execute(query)
    con.commit()
    data = cursor.fetchall()
    print("Updated Details:")
    for row in data:
         print('AuthorID: {}, Fname: {}, Mname: {}, Lname:: {}' \
               .format(row[0], row[1], row[2], row[3]))
    
    con.rollback()
    print("Formerly:")
     for row in data:
         print('AuthorID: {}, Fname: {}, Mname: {}, Lname:: {}' \
               .format(row[0], row[1], row[2], row[3]))
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')