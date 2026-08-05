import numpy as np
import pandas as pd

data={
    'Player':['Virat Kohli','Steve Smith','Joe Root','Kane Williamson','Babar Azam','Rashid Khan','Ben Stokes','David Warner','Shakib Al Hasan','Trent Boult','Mitchell Starc','Jasprit Bumrah','Pat Cummins','Rashid Khan','Shaheen Afridi','Mujeeb Ur Rahman','Shadab Khan','Mohammad Nabi','Mustafizur Rahman','Yasir Shah'],
    'Team':['India','Australia','England','New Zealand','Pakistan','Afghanistan','England','Australia','Bangladesh','New Zealand','Australia','India','Australia','Afghanistan','Pakistan','Afghanistan','Pakistan','Afghanistan','Bangladesh','Pakistan'],
    'Matches':[254, 128, 149, 151, 83, 73, 95, 128, 87, 78, 85, 67, 65, 73, 50, 45, 60, 55, 40, 70],
    'Runs':[12169, 7540, 6109, 6173, 3808, 1234, 4020, 5452, 3807, 1234, 1456, 789, 1023, 1234, 567, 456, 678, 789, 345, 890],
    'Average':[59.07, 62.84, 50.45, 47.48, 56.83, 18.12, 36.91, 48.29, 38.17, 18.12, 19.23, 24.65, 25.57, 18.12, 22.68, 20.13, 21.45, 23.67, 17.25, 19.78],
    'Strike Rate':[93.17, 88.45, 85.67, 80.12, 89.34, 130.45, 75.23, 90.12, 78.56, 120.34, 110.45, 95.67, 92.34, 130.45, 85.67, 88.12, 82.34, 79.56, 75.23, 80.12]
}

df=pd.DataFrame(data)

print("Original Data:")
print(df)

print("\n Highest Runs:")
print(df[df['Runs'].max()==df['Runs']])

print("\n Average Strike Rate:")
print(df['Strike Rate'].mean())

print("\n Players Scoring more than 5000 runs:")
print(df[df['Runs']>5000])

print("\n Team wise Filtering:")
team=input("Enter the team name to filter players: ")
print(df[df['Team'].str.lower()==team.lower()])

print("\n Sort by Average:")
print(df.sort_values('Average',ascending=False))

df.to_csv("cricket_player_statistics.csv",index=False)