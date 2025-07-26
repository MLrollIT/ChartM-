from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = StringIO("""
Disease,2000,2010,2020
Heart Disease,24.5,22.8,32.1
Cancer,12.8,32.3,14.1
Diabetes,7.2,8.2,7.9
""")

df = pd.read_csv(data)

diseases = df["Disease"].values
years = df.columns[1:].values
values = df[years].values.T

width = 0.2

fig, ax = plt.subplots()

colors = ['red', 'blue', 'green']  # Define colors for each disease.

for i, disease in enumerate(diseases):
    bars = ax.bar(np.arange(len(years)) + i * width, values[:, i], width, label=disease, color=colors[i], edgecolor='black')
    ax.bar_label(bars)

ax.set_title("Disease Percentages Over the Years")
ax.set_xlabel("Year")
ax.set_ylabel("Percentage")
ax.set_xticks(np.arange(len(years)) + width)
ax.set_xticklabels(years)
ax.legend(loc="upper left")
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")