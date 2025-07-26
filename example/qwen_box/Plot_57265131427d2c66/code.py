from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = StringIO("""
Year,Number of Visits,Number of Books Borrowed
2014,5000,7000
2015,4600,6000
2016,4700,9000
2017,4400,6500
2018,7000,8000
2019,6900,12000
2020,4500,7000
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

x = np.arange(len(df["Year"]))

colors = ['red', 'green']  # Define colors for the lines

for i in range(1, df.shape[1]):
    line, = ax.plot(x, df.iloc[:, i], marker='o', linestyle='--', linewidth=2, 
                    color=colors[i-1], markersize=6, alpha=0.696, label=df.columns[i])
    for j in range(len(x)):
        ax.text(j, df.iloc[j, i], df.columns[i], ha='right', color=colors[i-1])

ax.set_xlabel('Year')
ax.set_ylabel('Counts')
ax.set_title('Number of Visits and Books Borrowed Over the Years')
ax.legend(loc='upper right', shadow=True)
ax.set_xticks(x)
ax.set_xticklabels(df["Year"])
ax.grid(True)
ax.set_facecolor('white') # Change the background color to white

plt.tight_layout()
plt.savefig("myplot.png")