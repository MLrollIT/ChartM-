import matplotlib.pyplot as plt

# x-axis values (list of holidays)
holidays = ['New Year', "Valentine's Day", 'Easter', 'Fourth of July', 'Halloween', 'Thanksgiving', 'Christmas']

# y-axis values (list of total online orders)
total_online_orders = [1500, 2000, 1800, 2200, 1900, 2300, 2500]

# Create stair plot
plt.step(holidays, total_online_orders)

# Set plot title and labels
plt.title('Online Shopping Behaviors During Major Holidays')
plt.xlabel('Holidays')
plt.ylabel('Total number of online orders')

# Set clipping state of the lines that contain the center point of the bounding box to True
plt.gca().set_clip_on(True)

# Set snap state of the lines that contain the center point of the bounding box to False
plt.gca().set_snap(False)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")