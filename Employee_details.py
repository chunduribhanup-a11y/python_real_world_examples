import numpy as np
import pandas as pd

data={
    'Employees':['Employee1','Employee2','Employee3','Employee4','Employee5','Employee6','Employee7','Employee8','Employee9','Employee10','Employee11','Employee12','Employee13','Employee14','Employee15','Employee16','Employee17','Employee18','Employee19','Employee20'],
    'Age':[22,23,24,21,20,29,34,23,35,46,44,33,44,23,27,26,25,43,42,29],
    'Department':['Cse','Ece','Aiml','IT','Iot','Eee','Aids','Mechanics','IT','Ecs','Cse','IT','Aiml','Ai','Iot','Eee','Aids','Mechanics','IT','Ecs'],
    'Salary':[35000,40000,23000,12000,34000,60000,70000,46000,90000,89000,120000,2300000,34000,360000,4800000,560000,78000,45600,480500,670000],
    'Experience':['3Years','1Years','3Years','2Years','4Years','5Years','6Years','7Years','8Years','9Years','10Years','3Years','1Years','3Years','2Years','4Years','5Years','6Years','7Years','8Years']
}

df=pd.DataFrame(data)

print("Original Data:\n")

print(df)

print("\n Average Salary:")
print(df['Salary'].mean())

print("\n Highest Salary:")
print(df[df['Salary'].max()==df['Salary']])

print("\n Lowest Salary:")
print(df[df['Salary'].min()==df['Salary']])

print("Employee Earning more than 60000:")
print(df[df['Salary']>60000])

print("Employees in the IT Department:")
print(df[df['Department']=="IT"])

print("IT Employees Earning More than 70000:")
print(df[(df['Department']=="IT") & (df['Salary']>70000)])

print("Sorted Salarys From low to High:")
print(df.sort_values('Salary'))

df.rename(columns={'Salary':'Monthly_salary'},inplace=True)
print(df)

df.to_csv("Employee_Details.csv",,index=False)