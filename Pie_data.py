import matplotlib.pyplot as plt
import pandas as pd

data={
    'Department':['AI','AIML','CSE','ECE','EEE'],
    'Students':[300,350,250,180,90]
    }

df=pd.DataFrame(data)

plt.figure(figsize=(8,5))

explode=[0,0.1,0,0.1,0]

colors=[
    'red',
    'blue',
    'green',
    'orange',
    'pink']

plt.pie(
    df['Students'],
    labels=df['Department'],
    colors=colors,
    shadow=True,
    startangle=90,
    explode=explode,
    autopct="%1.1f%%"
    )

plt.title("Students Enrolled in Different Departments")

plt.show()