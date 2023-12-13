# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:52:01 2022

@author: Kriti
"""

#LIBRARY.py

import mysql.connector as mc
import day2
#import csv
connection  =   mc.connect  (  host  =   '127.0.0.1',
                        user  =  'kritika',
                        database  =   'newdb',
                        password   =   'Ikittu44#'  )
    
#Check if connection is established
if   connection.is_connected(): 
    print  (  'connection established'  )
cursor  =  connection.cursor()

#Create table nbook
'''
cursor.execute  (  "create table nbook ( BOOK_ID  int (5)  not  null  primary  key ,\
                                    NAME_OF_BOOK  varchar  (60) , NAME_OF_AUTHOR  varchar(50) ,\
                                    GENRE varchar (30), FORMAT  varchar  (10) , \
                                    PUBLISHER varchar (30) , NO_OF_COPIES  int (4) default 4, \
                                    NO_OF_COPIES_AVAI int (4) default 4)")

    
#To insert records in table nbook
file_name  =  open  (  "books.csv","r"  )

csv_reader  =  csv.reader  (  file_name  )


for row in csv_reader:
    
    query = f'insert into nbook values({row[0]},"{row[1]}","{row[2]}","{row[3]}","{row[4]}","{row[5]}", 4, 4);'
   
    cursor.execute ( query )
    connection.commit()


#Create table Students
cursor.execute  (  "create table students ( ADM_NO  int (4)  not  null  primary  key ,\
                                    NAME_OF_STUDENT  varchar  (50) , CLASS  int (2), SECTION  varchar  (1) ,\
                                    NAME_OF_BOOK_ISSUED  varchar(100) , DATE_OF_ISSUE  varchar  (10) ,\
                                    DUE_DATE_OF_RETURN  varchar (10) , DATE_OF_RETURN  varchar (10), \
                                    BOOK_ID int(5), EXTRA_CHARGES int(4))")
'''

#Create a menu
def   menu():
    print  (  "\t\t\t MENU" , \
          "1.  INSERT RECORD IN NBOOK" , \
         "2.  INSERT RECORD IN STUDENT" , \
         "3.  CHECK IF BOOK IS AVAILABLE" , \
          "4.  DELETE RECORD IN NBOOK" , \
          "5.  DELETE RECORD IN STUDENT" , \
          "6.  VIEW RECORD OF STUDENTS WHO HAVEN'T RETURNED BOOKS" , \
          "7.  VIEW RECORD OF A SPECIFIC STUDENT", \
          "8.  VIEW RECORD OF A SPECIFIC BOOK",\
          "9.  INSERT RETURN DATE OF BOOK" , \
          "10. PAYMENT BY STUDENT FOR DELAY IN RETURN" , \
          "11. VIEW ALL RECORDS OF NBOOK" , \
          "12. VIEW ALL RECORS OF STUDENTS" , \
          "13. EXIT" , sep="\n")

#Create delete function to delete records of students who have retured their books
def delete(): 
    
    cursor.execute ( 'delete from students where  DATE_OF_RETURN!="NULL"' ) 
    connection.commit()

#Loop for menu- driven program
while True:
    
    menu()
    x = int(input("SELECT ANY ONE-"))
    
    #To insert record in table nbook 
    if x == 1:
        
        while True: 
            
            cursor.execute  (  "select count(*) as total_records from nbook"  )
            result  =  cursor.fetchall()

            for r in result: 
                
                print  (  "TOTAL RECORDS ARE {}. KINDLY START INSERTING BOOK ID AFTER {}".format(r[0],r[0]))
            
            book_id = int ( input ( "ENTER BOOK ID-" ))
            book_name = input ( "ENTER NAME OF BOOK-" )
            auth_name = input ( "ENTER NAME OF AUTHOR-" )
            genre = input("ENTER GENRE OF THE BOOK-")
            form = input ( "ENTER FORMAT-" )
            pub = input ( "ENTER PUBLISHER-" )
            no_copies = int ( input ( "ENTER NO OF COPIES AVAILABLE-"))
            
            if book_id >= r[0]:
                
                query1 =  f'insert into nbook values({book_id}, "{book_name}", "{auth_name}",\
                                "{genre}","{form}", "{pub}", {no_copies}, {no_copies})'
    
                cursor.execute(query1)
                connection.commit()
            
                print("RECORD ADDED SUCCESSFULLY")
            
                cont_in = input("PRESS 'Y' TO CONTINUE INSERTION OR PRESS ANY OTHER KEY TO EXIT- ")
   
                if cont_in.upper() == "Y":   
                    continue
                else: 
                    break 
            else:
                print("SORRY, DUPLICATE ENTRY")
    
    
   #To insert record in table students
    elif x == 2:
       
        while True: 
            
            adm_no = int ( input ("ENTER ADM NO. OF STUDENT-" ))
            
            cursor.execute  (  f'select date_of_return from students where adm_no = {adm_no}'  )
            result1 = cursor.fetchall()
            
            if result1 == []: 
            
                book_id=int ( input ( "ENTER BOOK ID-" ))
        
                cursor.execute ( f'select NO_OF_COPIES_AVAI from nbook where BOOK_ID={book_id}')
                result2 = cursor.fetchall()
            
                index = result2 [0][0]
        
                if index == 0:
                    
                    print("SORRY, BOOK IS UNAVAILABLE CURRENTLY")
                
                elif index > 0: 
                    
                    stu_name  =  input ( "ENTER NAME OF STUDENT-" )
                    clas = int ( input ( "ENTER CLASS-" ))
                    sec = input ( "ENTER SECTION-" )
                    book_name = input ( "ENTER NAME OF BOOK ISSUED-" )
                    cur_date = input ( "ENTER DATE OF ISSUE (FORMAT-DD-MM-YYYY)-" )
        
                    query1 = f'insert into students values({adm_no}, "{stu_name}", {clas},"{sec}",\
                                   "{book_name}", "{cur_date}", "NULL", "NULL", {book_id}, 0)'

                    cursor.execute(query1)
                    connection.commit()
                    
                    cursor.execute  (  f'update nbook set NO_OF_COPIES_AVAI={index-1}\
                                                 where BOOK_ID={book_id}')
                    connection.commit()
        
                    print("RECORD ADDED SUCCESSFULLY")
        
                    due_date  =   day2.cal_due_date(cur_date)
                    
                    cursor.execute  (  f'update students set DUE_DATE_OF_RETURN="{due_date}"\
                                                 where ADM_NO = {adm_no}')
                    connection.commit()
            
                    cont_in = input  ( "PRESS 'Y' TO CONTINUE OR PRESS ANY OTHER KEY TO EXIT- " )
                    
                    if cont_in.upper() == "Y":   
                        continue
                    else:
                        break
                    
            else: 
                print  (  "SORRY, PREVIOUS BOOK IS NOT RETURNED YET"  )
                break
            
                
    #To check if book is currently available in Library            
    elif x == 3: 
        
        book_name =  input  ( "ENTER NAME OF BOOK-" )
        cursor.execute   (   f'select NO_OF_COPIES_AVAI from nbook \
                                      where NAME_OF_BOOK = "{book_name}"'  )
       
        result  =  cursor.fetchall()

        index  =  result[0][0]
            
        if index == 0:
            print  (  "BOOK IS NOT AVAILABLE  "  )
        else:
            print  (  "YES {} BOOKS IS/ARE AVAILABLE".format(index)  )
            
            
    #To delete a record in table nbook        
    elif x == 4: 
        
        book_id  =  int  (  input  (  "ENTER BOOK ID TO DELETE THE BOOK-" ))

        cursor.execute  (  f'delete from nbook where BOOK_ID = {book_id}'  )
        connection.commit()
        
        print  (  "RECORD DELETED SUCCESSFULLY"  )
        
        
    #To delete a record in table students
    elif x == 5:
        
        adm_no  =  int  (  input  (  "ENTER ADM NO. TO DELETE THE RECORD-"  ))
        
        cursor.execute  (  f'delete from students where ADM_NO = {adm_no}'  ) 
        connection.commit()
        
        print  (  "RECORD DELETED SUCCESSFULLY"  )
        
        
    # To view record of students who haven't returned previous book yet   
    elif x == 6:
        
        cursor.execute  (  'select * from students where DATE_OF_RETURN = "NULL"'  )
        result  =  cursor.fetchall()
            
        if result == []:
             print  (  "NO RECORD FOUND"  )
        
        else:
            for r in result:    
                print(r) 
                
     
    #To view record of a particular student 
    elif x==7:
        
        adm_no  =  int  (  input  (  "ENTER ADM_NO OF STUDENT-"  ))
        
        cursor.execute  (  f'select * from students where adm_no = {adm_no}'  )
        result  =  cursor.fetchall()
        
        for r in result: 
            print  (  r  )
            
        
    #To view record of a particular book 
    elif x == 8:
        
        book_id  =  int  (  input  (  "ENTER ID OF BOOK-"  ))
        
        cursor.execute  (  f'select * from nbook where book_id = {book_id}'  )
        result  =  cursor.fetchall()
       
        for r in result: 
            print  (  r  )
        
        
    #To insert return date of book in students table    
    elif x == 9:
        
        adm_no  =  int  (  input  (  "ENTER ADM NO OF STUDENT-"  ))
        date_ret  =  input  (  "ENTER RETURN DATE (FORMAT - DD-MM-YYYY)-"  )
        
        cursor.execute  (  f'update students set DATE_OF_RETURN = "{date_ret}" \
                                    where ADM_NO = {adm_no}'  )
        connection.commit()
        
        print  (  "DATE UPDATED"  )
        
        cursor.execute  (  f'select BOOK_ID from students where ADM_NO = {adm_no}'  )
        result  =  cursor.fetchall()
        
        index  =  result[0][0]
        
        cursor.execute  (  f'update nbook set NO_OF_COPIES_AVAI = NO_OF_COPIES_AVAI+1\
                                          where BOOK_ID = {index}'  )
                       
        cursor.execute  (  f'select DUE_DATE_OF_RETURN , DATE_OF_RETURN from students\
                                     where adm_no = {adm_no}'  )
        result1  =  cursor.fetchall()
        
        due_date  =  result1[0][0]
        ret_date   =   result1[0][1]
        
        total  =  day2.count_days  (  due_date , ret_date  )
        cursor.execute  (  f'update students set EXTRA_CHARGES = {total}\
                                     where ADM_NO = {adm_no}'  )
                       
        connection.commit()
        
        
    #Amount to be paid by student for delay in returning the book"
    elif x==10:  
        
        adm_no  =  int  (  input  (  "ENTER ADM_NO OF STUDENT-"  ))
        
        cursor.execute   (  f'select EXTRA_CHARGES from students where adm_no = {adm_no}'  )
        result  =  cursor.fetchall()
        
        r  =  result[0][0]
        print  (  "TOTAL AMOUNT TO BE PAID= Rs.",r  )
        
        
    #To view all records of table nbook    
    elif x == 11:
        
        cursor.execute  (  "select * from nbook"  )
        result  =  cursor.fetchall()

        for r in result: 
            print  (  r  )
            
            
    #To view all records of table students
    elif x == 12: 
        
        cursor.execute  (  "select * from students"  )
        result  =  cursor.fetchall()

        for r in result: 
            print  (  r  )
            
            
    #To exit the program        
    elif x == 13:
       break
    
    
    #If other than provided options are chosen error message will be printed
    else:
        print(  "CHOOSE ANOTHER OPTION"  )


#To close all functions running in background   
cursor.close()
connection.close()

print  (  'connection closed'  )