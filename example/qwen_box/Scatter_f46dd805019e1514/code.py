import matplotlib.pyplot as plt

# data points
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sunlight_duration = [4.5, 6.8, 7.2, 8.5, 10.3, 11.8, 12.6, 11.3, 9.6, 7.8, 6.1, 4.9]

# create scatter plot
plt.scatter(months, sunlight_duration)

# set the labels
plt.xlabel('Month')
plt.ylabel('Sunlight Duration (hours)')

# set the title
plt.title('Daily sunlight duration in Antarctica throughout a year')

# set the bounding box
bbox = dict(boxstyle="square", fc="white", ec="black", lw=2, alpha=0.5)

# add a shadow effect to the points that contain the center point of the bounding box
for i in range(len(months)):
    if months[i] == 6 and sunlight_duration[i] == 12:
        plt.scatter(months[i], sunlight_duration[i], marker='diamond', s=100, color='silver', edgecolors='black', linewidths=2, label='Center point')
        plt.annotate('Center point', (months[i], sunlight_duration[i]), xytext=(6.7, 6.7), textcoords='offset points', bbox=bbox, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color='black', lw=2))

# show the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")