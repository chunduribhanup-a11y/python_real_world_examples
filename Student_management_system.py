import numpy as np
import pandas as pd

data={
    'Roll No':['2473A39001','2473A39002','2473A39003','2473A39004','2473A39003','2473A39006','2473A39007','2473A39008','2473A39009','2473A39010','2473A39011','2473A39012','2473A39013','2473A39014','2473A39013'],
    'Name':['Hemanth','Srinivas','Rohit','Rakesh','Rohit','Ramesh','Karthik','Vijay','Ajay','Rahul','Arjun','Naveen','Praveen','Suresh','Praveen'],
    'Age':[20,21,22,23,22,np.nan,24,25,26,27,np.nan,28,31,30,31],
    'Branch':['CSE','ECE','EEE','CSE','EEE','ECE','CSE','EEE','ECE','CSE','EEE','ECE','ECE','EEE','ECE'],
    'Marks':[85,90,95,80,95,88,np.nan,92,89,np.nan,91,87,84,86,84],
    'Attendence':[90,85,80,95,80,67,89,34,77,56,np.nan,88,80,75,80]
}

df=pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("First 5 rows of DataFrame:")
print(df.head(5))

print("Last 5 rows of DataFrame:")
print(df.tail(5))

print("Count Missing Values:")
print(df.isnull().sum())

print("Fill Missing Marks:")
df['Marks'].fillna(df['Marks'].mean(),inplace=True)
print(df)

print("Fill Missing Attendence:")
df['Attendence'].fillna(75,inplace=True)
print(df)

print("Remove Duplicate Rows:")
df.drop_duplicates(inplace=True)
print(df)

print("Students scoring more than 85 marks:")
print(df[df['Marks']>85])

print("Students with Attendence less than 75:")
print(df[df['Attendence']<75])

print("Highest Marks:")
print(df['Marks'].max())

print("Lowest Marks:")
print(df['Marks'].min())

print("Average Marks:")
print(df['Marks'].mean())

df.to_csv('Student_data.csv',index=False)