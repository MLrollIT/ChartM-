# Import necessary libraries
import matplotlib.pyplot as plt

# Data
depths = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
temperatures = [28.3, 27.8, 27.5, 26.9, 26.5, 26.2, 25.8, 25.4, 25.0, 24.6]

# Create a scatter plot
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.scatter(temperatures, depths, color='blue')  # plot the data
plt.gca().invert_yaxis()  # invert the y-axis to show depth increasing downwards

# Set plot title and labels for axes
plt.title("Ocean Temperature Variation Over Depth")
plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (meters)")

# Modify the size of the scatter points that contain the center point of the bounding box
center_point = (26.5, 30)
plt.scatter(center_point[0], center_point[1], s=89, alpha=0.53)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")