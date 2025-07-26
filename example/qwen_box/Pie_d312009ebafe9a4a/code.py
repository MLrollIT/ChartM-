from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# The data
jobs = ['Doctors', 'Engineers', 'Teachers']
percentage = [40, 30, 30]

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Setting the background color of the figure
fig.patch.set_facecolor('gray')

# Creating the pie chart
wedges, texts, autotexts = ax.pie(percentage, explode=(0.1, 0, 0), labels=jobs, autopct='%1.1f%%', shadow=True, startangle=140, colors=['blue', 'orange', 'green'])

# Adding the legend
ax.legend(wedges, jobs, title='Professions', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Set the border thickness of the slices that contain the center point of the bounding box
for wedge in wedges:
    wedge.set_linewidth(1.6739803120152579)
    wedge.set_edgecolor('#8eee8b')

# Save the figure
plt.tight_layout()
plt.savefig('myplot.png')