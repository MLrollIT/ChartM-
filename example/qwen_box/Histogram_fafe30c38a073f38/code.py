# necessary libraries
import matplotlib.pyplot as plt
import numpy as np

#data
x = ["10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90-100"]
y = [5, 12, 8, 15, 20, 18, 10, 6, 4]


#creating figure and axis objects
fig, ax = plt.subplots()

#creating barplot 
ax.bar(x, y, color='b', alpha=0.7)

#setting labels and title
ax.set_xlabel('Marine Species Richness')
ax.set_ylabel('Frequency of Reef Areas')
plt.title('Marine Biodiversity in Reef Ecosystem')

#rotating x-axis labels for better readability
plt.xticks(rotation=45)

#adding shadow effect to bars that contain the center point of the bounding box
bbox = (3.92, 3.66)
shadow_color = 'gray'
shadow_offset = (3.92, 3.66)
shadow_alpha = 0.5
shadow_width = 3
shadow_height = 3

for i in range(len(x)):
    if i in [3, 4]:
        ax.bar(x[i], y[i], color='b', alpha=0.7, shadow=True, shadowprops=dict(color=shadow_color, offset=shadow_offset, alpha=shadow_alpha, width=shadow_width, height=shadow_height), clip_on=True)

#showing the plot
plt.tight_layout()
plt.savefig("figure.png")