from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
data = {
    "Religion": ["Christianity", "Islam", "Secular/Nonreligious/Agnostic/Atheist", "Hinduism",
                 "Buddhism", "Chinese Traditional Religion", "Ethnic Religions excluding some in separate categories", "Other"],
    "Percentage": [31, 24, 16, 15, 7, 5, 1, 1]
}

labels = data["Religion"]
sizes = data["Percentage"]

fig, ax = plt.subplots()

# Use explode to highlight the first slice of the pie chart
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

ax.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, 
       textprops={'size': 'smaller'}, radius=1.0, shadow=True, 
       labeldistance=1.1, pctdistance=0.8, startangle=150, colors=plt.cm.Paired.colors)

plt.title("Distribution of World Religions") # Add title
plt.legend(labels, title="Religions", loc="upper right") # Add legend

fig.set_facecolor('lightgray') # Set the background color to light gray
plt.tight_layout() # Adjust the layout
plt.savefig("myplot.png")