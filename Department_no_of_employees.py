import matplotlib.pyplot as plt
import pandas as pd

data={
    'Department':['IT','IOT','AI','FINANCE','MARKETING'],
    'Employees':[120,70,45,60,80]
    }

df=pd.DataFrame(data)

plt.figure(figsize=(8,5))
bars=plt.bar(df['Department'],df['Employees'],color=['red','green','pink','blue','orange'])

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        str(int(bar.get_height())),
        ha="center",
        va="bottom"
        )
    
plt.title("Employee Vs Departments")

plt.xlabel("Department")
plt.ylabel("Employees")

plt.grid(True)

plt.show()