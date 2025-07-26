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

# setting the rasterized state of the bars that contain the center point of the bounding box to True
plt.bar(x_labels, y_values, color='skyblue', rasterized=True)

# making those bars invisible by setting their visibility to False
plt.bar(x_labels, y_values, color='skyblue', rasterized=True, visible=False)

# displaying the plot
plt.tight_layout()
plt.savefig("figure.png")