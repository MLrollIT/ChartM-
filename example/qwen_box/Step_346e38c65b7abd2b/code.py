import matplotlib.pyplot as plt

# X-axis data points
countries = ['United States', 'United Kingdom', 'France', 'Germany', 'Italy', 'Spain', 'Australia', 'Japan']

# Y-axis data points
border_closing = [40, 25, 60, 75, 80, 70, 10, 5]

# Create the stair plot
plt.step(countries, border_closing, where='mid')

# Adding labels, title and a grid
plt.title('Popularity of Travel Destinations Based on Border Closings')
plt.xlabel('Countries')
plt.ylabel('Border Closings (0-100)')
plt.grid(True)

# Set the snap state of the lines that contain the center point of the bounding box to True
plt.gca().set_snap(True)

# Show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")