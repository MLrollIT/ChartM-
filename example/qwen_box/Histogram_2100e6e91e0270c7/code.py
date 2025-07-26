import matplotlib.pyplot as plt

# Given data points
microbial_abundance = [120, 135, 148, 155, 169, 178, 185, 192, 205, 212, 227, 235, 242, 256, 264, 278, 285, 
                       292, 305, 312, 326, 332, 345, 353, 367, 372, 388, 395, 402, 417, 422, 436, 443, 458, 
                       465, 472, 485, 492, 497, 500, 512, 527, 535, 548, 553, 568, 576, 584, 595, 606]

# Creating the histogram
plt.hist(microbial_abundance, bins=10, edgecolor='black')

# Setting the labels
plt.xlabel('Microbial Abundance (cells/cm³)')
plt.ylabel('Frequency')

# Setting the title
plt.title('Distribution of Oceanic Microbial Abundance in Sediments')

# Hide the bars that contain the center point of the bounding box
plt.bar([300], [350], color='black', alpha=0.5, edgecolor='black', linewidth=2)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")