from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Define the csv data
csv_data = """
Profession,Commute Time (mins),Year
Doctor,45,2010
Doctor,49,2011
Doctor,52,2012
Doctor,55,2013
Doctor,30,2014
Doctor,35,2015
Lawyer,20,2010
Lawyer,15,2011
Lawyer,10,2012
Lawyer,35,2013
Lawyer,30,2014
Lawyer,25,2015
Engineer,25,2010
Engineer,30,2011
Engineer,35,2012
Engineer,40,2013
Engineer,20,2014
Engineer,45,2015
Teacher,35,2010
Teacher,40,2011
Teacher,45,2012
Teacher,50,2013
Teacher,40,2014
Teacher,40,2015
Chef,30,2010
Chef,35,2011
Chef,30,2012
Chef,35,2013
Chef,40,2014
Chef,45,2015
"""

# Convert the csv data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Create a figure and an axes
fig, ax = plt.subplots()

# Iterate over the professions and plot the data
colors = ['blue', 'orange', 'green', 'red', 'purple']
markers = ['o', 'v', '^', '<', '>']
for i, profession in enumerate(df['Profession'].unique()):
    data = df[df['Profession'] == profession]
    ax.plot(data['Year'], data['Commute Time (mins)'], color=colors[i], marker=markers[i], markersize=5, label=profession, linestyle='-', linewidth=1.5, alpha=0.8)

# Set the title, labels, legend, and grid
ax.set_title('Commute Time by Profession Over Years', fontsize=20) # Change title font size to 20
ax.set_xlabel('Year', fontsize=16) # Change x-axis label font size to 16
ax.set_ylabel('Commute Time (mins)', fontsize=16) # Change y-axis label font size to 16
ax.legend()
ax.grid(True)

# Change the background color
ax.set_facecolor('lightgrey')

# Annotate each line at the end of the line
for line, name in zip(ax.lines, df['Profession'].unique()):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")