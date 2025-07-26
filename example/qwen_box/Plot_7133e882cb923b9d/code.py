from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = StringIO("""
Household,Vegetable Waste,Fruit Waste,Grain Waste
Household 1,50,60,70
Household 2,80,45,30
Household 3,90,35,20
Household 4,70,85,60
Household 5,40,25,100
""")

df = pd.read_csv(data, sep=",")

fig, ax = plt.subplots(facecolor='white')  # Change background to white

ax.plot(df['Household'], df['Vegetable Waste'], label="Vegetable Waste", color="red", linewidth=2, linestyle='-', marker='o', markersize=8, alpha=0.8)
ax.plot(df['Household'], df['Fruit Waste'], label="Fruit Waste", color="green", linewidth=2, linestyle='--', marker='v', markersize=8, alpha=0.8)
ax.plot(df['Household'], df['Grain Waste'], label="Grain Waste", color="blue", linewidth=2, linestyle='-.', marker='^', markersize=8, alpha=0.8)

for col in ["Vegetable Waste", "Fruit Waste", "Grain Waste"]:
    for x, y in zip(df['Household'], df[col]):
        ax.text(x, y, str(y))

ax.set_title('Waste Distribution per Household')
ax.set_xlabel('Household')
ax.set_ylabel('Waste (kg)')
ax.legend(loc='upper left', shadow=True)

ax.grid(False)  # Remove grid lines
plt.tight_layout()
plt.savefig("myplot.png")