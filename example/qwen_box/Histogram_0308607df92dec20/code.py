# importing necessary libraries
import matplotlib.pyplot as plt

# Setting X and Y data
x_labels = ['5-10', '10-20', '20-50', '50-100', '100-200', '200-500', '500-1000']
y_values = [12, 19, 27, 35, 24, 15, 8]

# creating a new figure
plt.figure(figsize=(10,5))

# plotting the bar chart
plt.bar(x_labels, y_values, color='skyblue')

# setting the title
plt.title('Galactic Black Hole Mass Analysis')

# setting x-axis label
plt.xlabel('Black Hole Mass Intervals (in Solar Masses)')

# setting y-axis label
plt.ylabel('Frequency of Black Holes')

# modifying the edge style and color of the bars that contain the center point of the bounding box
for bar in plt.gca().get_children():
    if isinstance(bar, plt.Rectangle):
        if bar.get_x() + bar.get_width() / 2 == 50:
            bar.set_edgecolor('#f28d95')
            bar.set_linestyle('dotted')

# displaying the plot
plt.tight_layout()
plt.savefig("figure.png")