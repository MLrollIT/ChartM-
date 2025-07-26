import matplotlib.pyplot as plt
import numpy as np

# Define the data
age_groups = ['Teens', 'Young Adults', 'Adults', 'Seniors']
pop = [45, 30, 20, 10]
hip_hop = [30, 20, 15, 5]
edm = [10, 15, 10, 5]
rnb = [5, 10, 20, 30]
rock = [5, 15, 25, 40]
other = [5, 10, 10, 10]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Make the stack plot
ax.stackplot(age_groups, pop, hip_hop, edm, rnb, rock, other, labels=['Pop','Hip Hop/Rap','EDM','R&B','Rock','Other'])

# Add legend, title, and labels
ax.legend(loc='upper left')
plt.title('Musical Preferences of Different Age Groups')
plt.xlabel('Age Groups')
plt.ylabel('Percentage of Listeners (%)')

# Add stroke to the area containing the center point of the bounding box
bbox = ax.bbox_to_anchor([0.5, 0.5, 0.3, 0.3])
ax.add_patch(plt.Rectangle((bbox.x0, bbox.y0), bbox.width, bbox.height, facecolor='#664caf', edgecolor='none', linewidth=2.01, fill=True, clip_on=False))

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")