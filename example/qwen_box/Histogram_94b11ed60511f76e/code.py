# necessary libraries
import matplotlib.pyplot as plt

# dataset
data = [32, 96, 45, 67, 76, 28, 79, 62, 43, 81, 70, 61, 95, 44, 60, 69, 71, 23, 69, 54, 76, 67, 82, 97, 26, 34, 18, 16, 59, 88, 29, 30, 66, 23, 65, 72, 20, 78, 49, 73, 62, 87, 37, 68, 81, 80, 77, 92, 81, 52, 43, 68, 71, 86]

# create histogram
plt.hist(data, bins = 10, edgecolor = 'black')

# create labels
plt.xlabel('Value Ranges')
plt.ylabel('Frequency')
plt.title('Data Points Histogram')

# modify the edge color of the bars that contain the center point of the bounding box
bbox = (50, 60, 60, 70)
plt.bar([bbox[0], bbox[2]], [bbox[1], bbox[3]], edgecolor = '#a2b830', color = '#770a0a', alpha = 0.497, label = 'Center Point')

# apply a soft glow effect to these bars
glow_color = '#b9fe9a'
plt.bar([bbox[0], bbox[2]], [bbox[1], bbox[3]], edgecolor = glow_color, color = glow_color, alpha = 0.497, label = 'Soft Glow')

# display the plot
plt.tight_layout()
plt.savefig("figure.png")