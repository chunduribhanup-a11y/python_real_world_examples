import matplotlib.pyplot as plt

month=['jan','feb','mar','apr','may','june']
sales=[30000,34000,23000,45000,56000,67000]
expenses=[20000,32000,10000,35000,40000,45000]

plt.plot(month,
         sales,
         color="blue",
         linestyle="-",
         marker="o",
         label="sales"
         )
plt.plot(month,
         expenses,
         color="red",
         linestyle="--",
         marker="s",
         label="expenses"
         )

plt.title("Company Sales Vs Expenses (6 Months)")
plt.xlabel("month")
plt.ylabel("Amount ($)")

plt.grid(True)
plt.legend()

plt.show()