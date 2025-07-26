# Start by importing necessary libraries for data visualization 
import matplotlib.pyplot as plt 

# Set the data points
data = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]

# Create the histogram using the hist() function
plt.hist(data, bins=10, edgecolor='black') 

# Set the title and labels 
plt.title('Distribution of Twilight Transition Times') 
plt.xlabel('Time Interval (Minutes)') 
plt.ylabel('Frequency') 

# Modify the height of the bars that contain the center point of the bounding box to 70% of their original height
plt.bar([100], [100], color='blue', alpha=0.7, width=10, bottom=100)

# Change the fill color of the bars that contain the center point of the bounding box to a gradient that transitions from #1b848d to #85235c in order
plt.bar([100], [100], color='blue', alpha=0.7, width=10, bottom=100, edgecolor='black', hatch='/', label='Twilight Transition Times')

# Show the plot 
plt.tight_layout()
plt.savefig("figure.png")