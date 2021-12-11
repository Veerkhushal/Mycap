

import pandas as pd
l1=[]
columns=["Name"]
while True:
    subject=input("Enter subject name ")
    if subject=="":
        break
    columns.append(subject)

while True:
    l2=[]
    name=input("Enter name of student ")
    if name=="":
        break
    l2.append(name)
    
    for column in range(1,len(columns)):
        data=int(input("Enter marks of {} ".format(columns[column])))
        l2.append(data)
    l1.append(l2)    
dataframe=pd.DataFrame(l1)
dataframe.columns=columns 
dataframe.to_csv("marks.csv")