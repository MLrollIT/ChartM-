from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

labels = ["Movies", "Music", "Books"]
sizes = [40, 30, 30]
explode = (0.1, 0, 0)  # only "explode" the 1st slice (i.e. 'Movies')

fig, ax = plt.subplots()

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, labeldistance=1.15, pctdistance=0.6)

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Entertainment Preferences") # Add title
plt.legend(labels, title="Entertainment Forms", loc="upper right") # Add legend

fig.patch.set_facecolor('lightgray') # Set the background color to light gray

plt.tight_layout() # Fit the figure into the tight layout

plt.savefig("myplot.png")