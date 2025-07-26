import matplotlib.pyplot as plt

# data points
depth = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
current_speed = [0.5, 0.8, 1.2, 1.5, 1.7, 1.5, 1.2, 0.8, 0.5, 0.2]

# create a stair plot
plt.step(depth, current_speed, where='mid')

# set the limit for x-axis and y-axis 
plt.xlim(0, 100)
plt.ylim(0, 2)

# specify labels and title
plt.xlabel('Depth (in meters)')
plt.ylabel('Current Speed (in knots)')
plt.title('Ocean Currents Data Visualization')

# modify the linewidth of the portion of the step chart that contains the center point of the bounding box
plt.plot([40, 40], [1.5, 1.7], linewidth=0.87, zorder=16, offset=[3.82, 2.12])

# show the plot

plt.tight_layout()
plt.savefig("figure.png")