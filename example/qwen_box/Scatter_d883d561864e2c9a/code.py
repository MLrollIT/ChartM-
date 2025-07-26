import matplotlib.pyplot as plt

# temperature data
temp_data = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]

# revenue data
revenue_data = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]

# create the scatter plot
plt.scatter(temp_data, revenue_data)

# title and labels
plt.title("Revenue Earned vs. Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Revenue Earned ($)")

# find the center point of the bounding box
bbox_center = (22.1, 522)

# find the index of the center point in the data
center_index = temp_data.index(bbox_center[0])

# change the color of the scatter points that contain the center point of the bounding box
plt.scatter(temp_data, revenue_data, c='black')
plt.scatter(temp_data[center_index], revenue_data[center_index], c='#abc053')

# show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")