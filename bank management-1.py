# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:01:44 2021

@author: HP
"""


import mysql.connector as a 
import matplotlib.pyplot as plt
import pandas as pd
con=a.connect(host='localhost',user='root',passwd='veerkhushal',database='bank')
print("\t\t............................................................")
print("\t\t\t\t*****WELCOME TO BANK MANAGEMENT SYSTEM*****")
print("\t\t............................................................")
print("\n\t\t\t\t\t******STAR BANK OF BIKANER*******")
def OPEN_ACCOUNT():
    n=input('Enter Name:')
    ac=input('Enter Account No:')
    db=input('Enter Date Of Birth:')
    p=input('Enter Phone:')
    ad=input('Enter Address:')
    ob=int(input('Enter Opening Balance:'))
    d1=(n,ac,db,p,ad,ob)
    d2=(n,ac,ob)
    s1='insert into account values(%s,%s,%s,%s,%s,%s)'
    s2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(s1,d1)
    c.execute(s2,d2)
    con.commit()
    print("data entered successfully")
    start()
def DEMO_AMO(): #DEPOSITE AMOUNT
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No:")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone() #(1000,)
    tam=myresult[0]+am
    sql="update amount set balance=%s where ac no=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    start()
def WITHAM(): #WITHDRAW
    am=int(input("Enter Amount:"))
    ac=input('Enter Amount No:')
    a="select balance from amount where acno=%s" 
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0] -am
    sql="update amount set balance=%s where ac no=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    start()
def BALANCE():
    ac=input('Enter Amount No:')
    a="select balance from amount where acno=%s"    
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("balance for account:",ac,"is",myresult[0])
    start()
def DESPACC():
    ac=input('Enter Amount No:')
    a="select * from amount where acno=%s"    
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone() 
    for i in myresult :
        print(i,end=" ")
    start()
def DELETEACC():
    ac=input('Enter Account No:')
    s1="delete from account where acno=%s"
    s2="delete from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(s1,data)
    c.execute(s2,data)
    con.commit()
    print("data deleted successfully")
    print("------------RESTART-------" )
    start()
def pie_plot():
    print('pie plot')
    df=pd.read_sql("select * from account",con)
    print(df)
    plt.title('debit,credit,balance')
    z=eval(input('enter amount of debit,credit,balance in sq bracket'))
    color=['red','green','blue']
    items=['debit','credit','bal']
    expl=[0.2,0,0]
    plt.pie(z,color,labels=items,explode=expl,autopct="%5.1f%%")
    plt.show()
    start()
def bar_plot():
    print('bar_plot')
    df=pd.read_sql("select * from account",con)
    print(df)
    x=df['AccountNo']
    y=df['OpeningBalance']
    plt.xlabel('account no.',fontsize=14,color="r")
    plt.ylabel('balance',fontsize=14,color="r")
    plt.title('balance of the account holders',fontsize=14,color="blue")
    plt.xticks(fontsize=14,rotation=30)
    plt.bar(x,y,color='orange',width=0.20)
    plt.show()
    start()
def line_plot():
    print('line plot')
    df=pd.read_sql("select * from bank",con)
    x1=df['name']
    y1=df['bal']
    plt.xlabel('Name of account holder')
    plt.ylabel('Balance')
    plt.title('Balance in these account holder')
    plt.plot(x1,y1,color='r',linewidth=5,marker='0',marketfacecolor='blue')
    plt.show()
    start()
def EXIT():
    print("THANK YOU ")
def start():
    print("""
          1.OPEN NEW ACCOUNT
          2.DEPOSIT AMOUNT
          3.WITHDRAW AMOUNT
          4.BALANCE ENQUIRY
          5.DISPLAY CUSTOMER DETAILS
          6.DELETE AN ACCOUNT
          7.pie_plot
          8.bar_plot
          9.line_plot
          10.exit""")
    choice=input("Enter Task No:")
    if(choice =="1"):
        OPEN_ACCOUNT()
    elif(choice=="2"):
        DEMO_AMO()
    elif(choice=="3"):
        WITHAM()
    elif(choice=="4"):
        BALANCE()
    elif(choice=="5"):
        DESPACC()
    elif(choice=="6"):
        DELETEACC()
    elif(choice=="7"): 
        pie_plot()
    elif(choice=="8"):
        bar_plot()
    elif(choice=="9"):
        line_plot()
    elif(choice=="10"):
        EXIT()
    else:
        print("SORRY---INVALID CHOICE try again.....")
        start()
start()        

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    