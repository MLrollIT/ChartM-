import matplotlib.pyplot as plt

# Temperatures and Frequency 
temp_intervals = ['5-8', '8-11', '11-14', '14-17', '17-20', '20-23', '23-26']
frequency = [12, 28, 42, 50, 38, 25, 10]

plt.figure(figsize=(10, 6))  
plt.hist(range(len(frequency)), weights=frequency, bins=7, alpha=0.75, color='steelblue',edgecolor='black')

# Set x-axis labels as Temperature intervals
plt.xticks(range(len(frequency)), temp_intervals)

# xlabel and ylabel
plt.xlabel('Temperature Intervals in °C')
plt.ylabel('Frequency of Temperature Readings')

# set a title 
plt.title('Ocean Currents and Marine Life Biodiversity')

# display the plot
plt.tight_layout()
plt.savefig("figure.png")

# Set the clipping box of the bars that contain the center point of the bounding box to a region defined by the top-left corner at (252, 172), with a width of 344 and a height of 752, using matplotlib.transforms.Bbox.
bbox = plt.Bbox([[252, 172], [252 + 344, 172 + 752]])
plt.gca().set_clip_path(bbox.transform(plt.gca().transData))

# Update the line color of the Target_object to #98a468
plt.gca().lines[0].set_color('#98a468')

plt.show()