from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# The given data
data = StringIO("""\
Technology,2017,2018,2019,2020,2021
Smartphones,180,210,230,200,180
Desktop Computers,150,100,90,95,100
Laptops,100,120,110,130,110
Tablets,50,100,150,100,150
Smart Watches,10,20,30,20,10
""")
df = pd.read_csv(data)

fig, ax = plt.subplots()

# Set the parameters
linewidth = 1.5
# Updated color to shades of blue
color = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087']
marker = ['o', 'v', '^', '<', '>']
markersize = 5
alpha = 0.7
linestyle = ['-', '--', '-.', ':', '-']

# Plot the lines
for i, column in enumerate(df.columns[1:]):
    ax.plot(df["Technology"], df[column], color=color[i], linewidth=linewidth, linestyle=linestyle[i], 
            marker=marker[i], markersize=markersize, alpha=alpha, label=column)
    for j, value in enumerate(df[column]):
        ax.text(j, value, str(value), ha='center', va='bottom', color=color[i])  # Text color also updated

# Set the title and labels
ax.set_title("Usage of Different Technologies from 2017 to 2021")
ax.set_xlabel("Technology")
ax.set_ylabel("Usage")
ax.legend()

# Add grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

plt.tight_layout()

# Save the figure
plt.savefig('myplot_blue_shades.png')