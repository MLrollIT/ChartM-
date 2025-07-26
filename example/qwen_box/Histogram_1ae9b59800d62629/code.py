import matplotlib.pyplot as plt
import numpy as np

# Our bins will be every 15 minutes
bins = np.arange(0, 165, 15) 

# Reconstructed data with the given frequencies
data = np.repeat(np.arange(15, 165, 15), [800, 600, 400, 300, 200, 150, 100, 70, 50, 30]) 

plt.hist(data, bins = bins, edgecolor='black', alpha=0.7)
plt.xticks(bins)

plt.xlabel('Delay Ranges (minutes)')
plt.ylabel('Frequency of Flights')
plt.title('Distribution of Flight Delays')

# Change the edge style of the bars that contain the center point of the bounding box to 'dashed' and set their edge color to '#946655'.
for bar in plt.gca().patches:
    if bar.get_x() + bar.get_width() / 2 == 30:
        bar.set_edgecolor('#946655')
        bar.set_edgestyle('dashed')

plt.tight_layout()
plt.savefig("figure.png")