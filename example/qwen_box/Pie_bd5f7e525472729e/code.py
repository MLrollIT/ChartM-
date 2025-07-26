from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

data = {"Year": ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"],
        "Population Growth Percentage": [12, 15, 13, 10, 9, 14, 11, 16]}

df = pd.DataFrame(data)

labels = df['Year']
sizes = df['Population Growth Percentage']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. '2010')

fig, ax = plt.subplots()

ax.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Population Growth Percentage per Year")  # Add title
plt.legend(labels, title="Year", loc="upper right")  # Add legend
fig.patch.set_facecolor('gray')  # set the background color to gray

plt.tight_layout()
plt.savefig("myplot.png")