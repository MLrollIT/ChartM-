from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# CSV data
data = {
    "Area of Genetic Engineering": ["Crispr Technology", "Gene Therapy", "Genetic Modification", "Genome Sequencing", "Synthetic Biology", "Bioinformatics"],
    "Percentage": [35, 25, 20, 10, 5, 5]
}

# Prepare pie chart parameters
labels = data["Area of Genetic Engineering"]
sizes = data["Percentage"]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # slightly offset each slice
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'blue']

# Create figure and axes
fig, ax = plt.subplots()
fig.set_facecolor('gray')  # Set background color

# Plot pie chart
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140, labeldistance=1.05, pctdistance=0.85)

# Set title and legend
plt.title("Distribution of Genetic Engineering Areas")
plt.legend(labels, title="Genetic Engineering Areas", loc="upper right")

plt.tight_layout()  # Adjust layout
plt.savefig("myplot.png")