import matplotlib.pyplot as plt

# time intervals
time_intervals = ['1', '2', '3', '4', '5']

# values for gas, stars, dust in each time interval
gas =   [100, 90, 85, 80, 75]
stars = [50, 60, 55, 65, 70]
dust =  [20, 25, 30, 35, 40]

plt.figure(figsize=(10,7))

# create stackplot
plt.stackplot(time_intervals, gas, stars, dust, labels=['Gas','Stars','Dust'], colors=['blue','orange','green'])
plt.legend(loc='upper right')

# labeling the axes
plt.xlabel('Time Intervals')
plt.ylabel('Units')

# adding title to the plot
plt.title('Dynamics of a Galactic Collision across Time Intervals')

# set the clipping box for the area that contains the center point of the bounding box
bbox = plt.Bbox([[71, 50], [71 + 132, 50 + 161]])
plt.clipbox(bbox, facecolor='#51dddd', alpha=0.5)

plt.tight_layout()
plt.savefig("figure.png")