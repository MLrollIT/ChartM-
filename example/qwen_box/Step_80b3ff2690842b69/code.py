import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

# Data
years = [1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020]
crop_yield = [200, 198, 195, 192, 190, 185, 182, 180, 178, 175, 172]

# Create a new figure
plt.figure(figsize=[10,5])

# Create a stair plot
plt.step(years, crop_yield, where='post')

# Labeling the axes
plt.xlabel("Years")
plt.ylabel("Crop Yield (Million Metric Tons)")

# Title of the plot
plt.title("Impact of climate change on global crop yields (1970-2020)")

# Create a path for the area to be filled
path = mpath.Path([[1975, 200], [1975, 198], [1980, 198], [1980, 195], [1985, 195], [1985, 192], [1990, 192], [1990, 190], [1995, 190], [1995, 185], [2000, 185], [2000, 182], [2005, 182], [2005, 180], [2010, 180], [2010, 178], [2015, 178], [2015, 175], [2020, 175], [2020, 172]])
patch = mpatches.PathPatch(path, facecolor='none', edgecolor='black', lw=2)

# Add the path to the plot
plt.gca().add_patch(patch)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")