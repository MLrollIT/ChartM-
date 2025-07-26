from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
regions = ['North America', 'Asia', 'Europe', 'South America', 'Africa']
percentages = [15, 50, 20, 10, 5]

fig, ax = plt.subplots()

# Pie chart parameters
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'North America')
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'grey']

# Set font size for pie chart labels and autopct
plt.rcParams['font.size'] = 14

ax.pie(percentages, explode=explode, labels=regions, colors=colors, autopct='%1.1f%%',
       shadow=True, startangle=140, pctdistance=0.85, labeldistance=1.2)

plt.title("Percentage Distribution of Regions")  # Add title
# Set font size for legend
plt.legend(regions, title="Regions", loc="upper right", title_fontsize=12, fontsize=12)

# Draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Set the background color of the chart figure
fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig("myplot.png")