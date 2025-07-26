from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# The given data
data = StringIO("""
Year,Earthquake,Tsunami,Hurricane
2014,56,44,70
2015,52,48,75
2016,41,55,80
2017,40,62,85
2018,70,60,78
2019,65,77,70
2020,60,80,65
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

# Set the parameters
linewidth = 1.5
color = ['red', 'blue', 'green']
marker = ['o', 'v', '^']
markersize = 5
alpha = 0.7
linestyle = ['-', '--', '-.']

# Plot the lines
for i, column in enumerate(df.columns[1:]):
    ax.plot(df["Year"], df[column], color=color[i], linewidth=linewidth, linestyle=linestyle[i], 
            marker=marker[i], markersize=markersize, alpha=alpha, label=column)
    for j, value in enumerate(df[column]):
        ax.text(df["Year"][j], value, str(value), ha='center', va='bottom')

# Set the title and labels
ax.set_title("Natural Disasters Over the Years")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Occurrences")
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

# Adjust the transparency of the lines associated with the center point of the bounding box to 0.88
bbox = plt.Bbox([[386, 300], [386 + 191, 300 + 623]])
ax.add_artist(ax.transData.transform_bbox(bbox))
ax.add_line(ax.Line2D([386, 386 + 191], [300, 300 + 623], color='black', alpha=0.88, linewidth=1.5))

# Save the figure
plt.savefig('myplot.png')