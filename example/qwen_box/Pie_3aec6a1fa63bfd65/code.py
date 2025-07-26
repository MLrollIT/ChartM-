from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
Newspaper,Percentage
"The New York Times","20%"
"The Washington Post","15%"
"The Wall Street Journal","25%"
"USA Today","10%"
"The Los Angeles Times","10%"
"Chicago Tribune","5%"
"The Boston Globe","5%"
"San Francisco Chronicle","5%"
"Others","5%"
"""))

df = pd.read_csv(data, sep =",")
df['Percentage'] = df['Percentage'].str.rstrip('%').astype('float')

labels = df['Newspaper'].values
sizes = df['Percentage'].values

fig, ax = plt.subplots()

# Additional parameters
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  
color = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c2f0c2']

ax.pie(sizes, labels=labels, autopct='%.0f%%', startangle=90, explode=explode, colors=color, pctdistance=0.85, shadow=True)

#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  
plt.tight_layout()

plt.title("Readership Distribution of Newspapers") # Add title
plt.legend(labels, title="Newspapers", loc="upper right") # Add legend

fig.patch.set_facecolor('#ADD8E6') # Change the background color of the chart figure to light blue (hex color code #ADD8E6)

# Change the clipping state of the slice that contains the center point of the bounding box to False
ax.pie(sizes, labels=labels, autopct='%.0f%%', startangle=90, explode=explode, colors=color, pctdistance=0.85, shadow=True, wedgeprops=dict(clipping_on=False))

# Update the label of that same slice to 'A new Label'
ax.pie(sizes, labels=labels, autopct='%.0f%%', startangle=90, explode=explode, colors=color, pctdistance=0.85, shadow=True, wedgeprops=dict(clipping_on=False), labels=['A new Label'])

plt.savefig("myplot.png")