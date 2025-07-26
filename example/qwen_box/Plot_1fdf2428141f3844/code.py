from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# The given data
data = """Year,Condominiums,Houses,Townhouses
2000,3000,5000,4000
2001,3500,7000,4500
2002,5000,4500,4800
2003,4500,4800,4200
2004,4000,6000,4400
2005,5000,5500,4600
2006,7000,5300,4800
2007,6600,5000,5000
2008,5700,4400,5200"""

df = pd.read_csv(StringIO(data))

fig, ax = plt.subplots()

# Set the parameters
linewidth = 1.5
# Change the colors here
color = ['#1f77b4', '#ff7f0e', '#2ca02c']  # New color scheme: blue, orange, green
marker = ['o', 'v', '^']
markersize = 5
alpha = 0.7
linestyle = ['-', '--', '-.']

# Plot the lines with new colors
for i, column in enumerate(df.columns[1:]):
    ax.plot(df["Year"], df[column], color=color[i], linewidth=linewidth, linestyle=linestyle[i], 
            marker=marker[i], markersize=markersize, alpha=alpha, label=column)
    for j, value in enumerate(df[column]):
        ax.text(j, value, str(value), ha='center', va='bottom')

# Set the title and labels
ax.set_title("Property price trends over the years")
ax.set_xlabel("Year")
ax.set_ylabel("Price")
ax.legend()

# Add grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Annotate each line at the end of the line with the corresponding legend label using new colors
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')