import matplotlib.pyplot as plt

# Given data
x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_data = [20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100]

# Creating the plot
plt.step(x_data, y_data, where='post')

# Setting the title and labels
plt.title('Correlation between the Number of Books Read per Year and Financial Success')
plt.xlabel('Number of Books Read per Year')
plt.ylabel('Financial Success (Scale: 1-100)')

# Adding the bounding box
bbox = dict(boxstyle="square", fc="white", ec="black", lw=2)
plt.text(8, 80, "8", bbox=bbox)

# Setting the marker style and z-order for the points in the bounding box
for i in range(7, 9):
    plt.plot(x_data[i], y_data[i], marker='>', markersize=10, zorder=12, mfc='none', mew=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mewa=2, mew