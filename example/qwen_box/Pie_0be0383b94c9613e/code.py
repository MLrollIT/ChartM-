from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
labels = ['1960s', '1970s', '1980s', '1990s']
sizes = [25, 30, 20, 25]

fig, ax = plt.subplots()

# Make the pie chart
explode = (0.1, 0, 0, 0)  # only "explode" the 1st slice (i.e. '1960s')
ax.pie(sizes, explode=explode, labels=labels, autopct='%.0f%%', shadow=True, startangle=90, pctdistance=0.85, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

# Draw a circle at the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

plt.title("Decade Distribution") # Add title
plt.legend(labels, title="Decades", loc="upper right") # Add legend

# set the background color of the figure
fig.set_facecolor("gray")

plt.tight_layout()
plt.savefig("myplot.png")