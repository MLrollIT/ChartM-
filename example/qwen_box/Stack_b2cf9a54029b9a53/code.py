import matplotlib.pyplot as plt

# years from 2010 to 2020
years = list(range(2010, 2021))

# Carbon emissions from traditional vehicles
emission_traditional = [500, 490, 480, 470, 460, 450, 440, 430, 420, 410, 400]

# Carbon emissions from electric vehicles
emission_electric = [20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 170]

plt.stackplot(years, emission_traditional, emission_electric, labels=['Traditional Vehicles','Electric Vehicles'])

plt.legend(loc='upper right')
plt.title('Carbon Emissions from Traditional and Electric Vehicles in a city (2010 - 2020)')
plt.xlabel('Years')
plt.ylabel('Carbon Emissions in metric tons')
plt.tight_layout()

# Set the snap state to True for the area that contains the center point of the bounding box
plt.gca().set_snap(True)

# Adjust the z-order to 11 and apply a shadow effect with an offset of (3.63, 3.81), using a shadow color blue
bbox = plt.gca().bbox
bbox = bbox.transformed(plt.gca().transData.inverted())
bbox = bbox.get_points()
bbox[0] += (3.63, 3.81)
bbox[1] += (3.63, 3.81)
bbox = plt.Rectangle((bbox[0][0], bbox[0][1]), bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1], zorder=11, facecolor='none', edgecolor='blue', clip_on=False)
plt.gca().add_patch(bbox)

plt.savefig("figure.png")