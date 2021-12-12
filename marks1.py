import pandas as pd
l1=[]
columns=["Name"]
while True:
    subject=input("Enter Subject Name")
    if subject=="":
        break
    columns.append(subject)
while True:
    try:
        l2=[]
        name=input("Enter Name of Student")
        l2.append(name)
        for column in range(1,len(columns)):
            data=int(input("Enter marks of {}".format(columns[column])))
            l2.append(data)
        l1.append(l2)
        ask=input("Do you want to Continue(Y/N)")
        if ask=="N"or ask=="n":
            break
    except:pass
dataframe=pd.dataframe(l1)
dataframe.columns=columns 
dataframe.to_csv("marks.csv")       