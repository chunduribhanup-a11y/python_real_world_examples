import numpy as np

students_results=np.random.randint(35,100,size=100)

print(students_results)

print("Highest Marks:",students_results.max())

print("Lowest Marks:",students_results.min())

print("Average Marks:",students_results.mean())

print("Number of students who passed (>=35):",np.sum(students_results>=35))

print("Number who scored 90 above:",np.sum(students_results>=90))

students_results.sort()

print("Top 5 numbers:",students_results[-6:-1])

print("Bottom 5 numbers:",students_results[0:6])