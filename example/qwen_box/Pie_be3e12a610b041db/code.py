from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Prepare data
labels = 'Pop', 'Rock', 'Country', 'Jazz'
sizes = [30, 25, 20, 25]
explode = (0.1, 0, 0, 0)  # "Pop" will be slightly exploded out from the center of the pie

# Create pie chart
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', 
       shadow=True, startangle=90, labeldistance=1.2, pctdistance=0.6, 
       colors=['red', 'blue', 'green', 'yellow'])

# Additional settings
ax.set_facecolor('lightblue')  # Change background color to light blue
plt.title("Music Genre Distribution")  # Set title
plt.legend(labels, title="Music Genres", loc="upper right")  # Add legend
plt.tight_layout()  # Tight layout

# Save the figure
plt.savefig("myplot.png")