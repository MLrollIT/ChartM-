from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
profession = ["Software Engineers", "Actors", "Doctors", "Teachers", "Farmers", "Chefs", "Mechanics", "Lawyers", "Artists"]
score = [56, 89, 67, 102, 73, 85, 92, 75, 66]
x = np.arange(len(profession))

# Create the figure and the axes
fig, ax = plt.subplots()

# Scatter plot with new fixed color
scatter = ax.scatter(x, score, c='blue', marker='o')  # Changed 'c=score, cmap='viridis'' to 'c='blue''

# Annotate data values above the point
for i, txt in enumerate(score):
    ax.annotate(txt, (x[i], score[i]), ha='center')

# Annotate each line at the end of the line with the corresponding legend label
for i, txt in enumerate(profession):
    ax.annotate(txt, (x[i], score[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Set labels and title
ax.set_xlabel('Profession')
ax.set_ylabel('Dietary Score')
ax.set_title('Dietary Score by Profession')

# Add grids and set background color
ax.grid(True)
ax.set_facecolor('lightgrey')

# Tight layout and save the figure
plt.tight_layout()
plt.savefig("myplot.png")