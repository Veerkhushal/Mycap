# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:22:13 2021

@author: HP
"""


# -*- coding: utf-8 -*-
import mysql.connector as sqltor

import pandas as pd
#create connection object
mycon=sqltor.connect(host='localhost',user='root',password='veerkhushal',database='school')
if mycon.is_connected():
    print('connected..')

crsr=mycon.cursor()
while True:
    print('Performing Connectivity Operation...')
    print('1.Select')
    print('2.Insert')
    print('3.Update')
    print('4.Delete')
    print('5.Exit')
    cnt=int(input('Select operation which u want..'))
    if cnt==1:
        crsr.execute('select * from student')
        data=crsr.fetchall()
        df=pd.DataFrame(data,columns=['Rollno','Name','Marks','Section','ProjectMarks'])
        cnt=crsr.rowcount
        print(df)
        print('Total no. of rows retrieved',cnt)
        #continue
    elif cnt==2:
        rllno=int(input('Enter rollno'))
        name=input('Enter name')
        mks=float(input('Enter marks'))
        sect=input('Enter section')
        pjt=input('Enter ProjectMarks')
        query='insert into student values({},"{}",{},"{}","{}")'.format(rllno,name,mks,sect,pjt)
        try:    
            crsr.execute(query)
            mycon.commit()
            print('Record inserted successfully...')
        except sqltor.IntegrityError:
            print(rllno,' is already exist..')
    elif cnt==3:
        rllno=int(input('Enter rollno'))
        name=input('Enter name')
        mks=float(input('Enter marks'))
        sect=input('Enter section')
        pjt=input('Enter ProjectMarks')
        query='update student set name="{}",marks={},section="{}",ProjectMarks="{}" where rollno={}'.format(name,mks,sect,pjt,rllno)
        crsr.execute(query)
        cnt1=crsr.rowcount
        if cnt1>0:    
            mycon.commit()
            print('Record Updated successfully...')
        else:    
            print('Rollno '+str(rllno)+' is not found..')
    elif cnt==4:
         rllno=int(input('Enter rollno'))
         query='delete from student where rollno={}'.format(rllno)
         crsr.execute(query)
         mycon.commit()
         print('Record Deleted successfully...')
    else:
        break

