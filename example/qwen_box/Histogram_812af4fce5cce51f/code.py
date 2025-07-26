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

# Set the face color of the bars that contain the center point of the bounding box to #ee976d
plt.bar([100], color='#ee976d', picker=False)

# Show the plot 
plt.tight_layout()
plt.savefig("figure.png")