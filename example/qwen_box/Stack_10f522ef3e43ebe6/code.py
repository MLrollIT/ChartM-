import matplotlib.pyplot as plt

# x-axis values - the epochs
epochs = [1, 2, 3, 4, 5]

# y-axis values - the distributions
dark_matter = [200, 190, 180, 175, 170]
galaxies = [100, 110, 120, 125, 130]
hot_gas = [50, 55, 60, 65, 70]

# start with a basic figure
plt.figure()

# stacked plot
plt.stackplot(epochs, dark_matter, galaxies, hot_gas, labels=['Dark Matter','Galaxies','Hot Gas'])

# labels
plt.xlabel("Epoch")
plt.ylabel("Units")

# title
plt.title("Distributions of Dark Matter, Galaxies and Hot Gas over different Epochs")

# legend
plt.legend(loc='upper right')

# set the transparency of the area that contains the center point of the bounding box to 0.01
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.25
bbox[1] = 0.25
bbox[2] = 0.35
bbox[3] = 0.35
plt.gca().set_position(bbox)

# enable the rasterized state for this area by setting it to True
plt.gca().rasterized = True

# display plot
plt.tight_layout()
plt.savefig("figure.png")