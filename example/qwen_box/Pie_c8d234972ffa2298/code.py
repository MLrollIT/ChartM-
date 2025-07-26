from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data to plot
labels = ['Movies', 'Music', 'Sports', 'Video Games', 'Books', 'Theater', 'Art Exhibits']
sizes = [20, 15, 10, 25, 15, 10, 5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple', 'pink', 'orange']
explode = (0.1, 0, 0, 0.1, 0, 0, 0)  # Exploding 1st and 4th slice

# Plotting the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title("Percentage Distribution of Forms of Entertainment")  # Set the title of the chart
plt.tight_layout()  # Adjust the layout
fig.patch.set_facecolor('gray')  # Set the background color to gray

# Modify the transparency and linewidth of the slices
for slice in ax.patches:
    slice.set_alpha(0.93)
    slice.set_linewidth(4.23)

plt.savefig("myplot.png")  # Save the figure