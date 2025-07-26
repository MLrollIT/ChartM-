import matplotlib.pyplot as plt

# Specifying data
cities = ['London', 'Sydney', 'Tokyo', 'Cairo', 'Moscow', 'Mumbai', 'New York', 'Rio de Janeiro', 'Vancouver', 'Johannesburg']
rainfall = [50, 70, 100, 20, 40, 120, 80, 90, 60, 30]
x = range(1, len(cities)+1)

# Creating a scatter plot
plt.scatter(x, rainfall)

# Defining labels
plt.xlabel('Cities')
plt.ylabel('Rainfall (mm)')
plt.title('Average Monthly Rainfall in Different Cities')

# Setting the locations and labels of the x-axis
plt.xticks(x, cities, rotation='vertical')

# Updating the size and shape of the scatter points that contain the center point of the bounding box
plt.scatter(x, rainfall, s=22, marker='triangle')

# Displaying the plot

plt.tight_layout()
plt.savefig("figure.png")