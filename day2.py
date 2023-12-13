# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:59:28 2022

@author: Kriti
"""

# User defined Python Library

def makestring(num):
    if num < 10:
        return '0' + str(num)
    else: 
        return str(num)

def check_leap_year(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            return False 
        return True
    

def cal_due_date(cur_date):
    
    
    list1 = [1,3,5,7,8,10,12]
    #list2 = [2,4,6,9,11]
    
    
    date = int(cur_date[0:2])
    month = int(cur_date[3:5])
    year = int(cur_date[6:])
    
    if (month) in list1:
        if date + 15 > 31:
            date = date + 15 - 31
            month += 1
        else:
            date += 15
        
        if month == 13:
            year += 1
            month = 1
    
    else:
        if month == 2:
            if check_leap_year(year):
                if date + 15 > 29:
                    date = date + 15 - 29
                    month += 1
                else:
                    date += 15
            if date + 15 > 28:
                date = date + 15 -28
                month += 1
        else:    
            if date + 15 > 30:
                date = date + 15 - 30
                month += 1
            
            else:
                date += 15
    

    return makestring(date) +"-" + makestring(month) +"-"+ makestring(year)

def count_days(cur_date, fin_date):

    list1 = [1,3,5,7,8,10,12]
        #list2 = [2,4,6,9,11]
        
        
    date = int(cur_date[0:2])
    new_date= int(fin_date[0:2])
    month = int(cur_date[3:5])
    new_month = int(fin_date[3:5])
    year = int(cur_date[6:])
    new_year = int(fin_date[6:])
    
    count = count1 = count2 = count3 = days = i = 0
    
    if month in list1:
        days = 31 - date
        
    elif month == 2:
        
        if check_leap_year(year):
            days = 29 - date
        else:
            days = 28 - date
    
    else:
        days = 30 - date
        
    if new_year == year:
        if month!= new_month:
            
            nu = new_month - month - 1
           
            for i in range(month+1 , new_month):
               
                if i in list1:
                    count+=1
               
                elif i==2:
                   
                    if check_leap_year(year):
                        days-=1
                    else:
                        days-=2
           
            days = (30*nu) + new_date + count + days
        else:
            nu=0
            days = new_date - date
    
    else:
        for i in range(year+1 , new_year):
            count+=1
            
            if check_leap_year(i):
                count1+=1
        
        nu = 12 - month 
        
        for i in range(month+1 , 13):
               
              if i in list1:
                    count2+=1
               
              elif i==2:
                   
                    if check_leap_year(year):
                        days-=1
                    else:
                        days-=2
        
        for i in range(1, new_month):
               
                if i in list1:
                    count3+=1
               
                elif i==2:
                   
                    if check_leap_year(new_year):
                        days-=1
                    else:
                        days-=2
        
        days=(30*nu) + days + (365*count) + count1 + count2 + count3 + (30*(new_month-1)) + new_date
    
    return days
   
#print(count_days('31-12-2019','28-02-2020'))
#print(cal_due_date("20-04-2022"))