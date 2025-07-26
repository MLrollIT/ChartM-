import matplotlib.pyplot as plt

# Given data
depth_labels = ['Surface', 'Epipelagic', 'Mesopelagic', 'Bathypelagic']
plankton = [20, 15, 30, 10]
fish = [30, 20, 25, 5]
cephalopods = [10, 5, 15, 2]
corals = [5, 2, 5, 1]
mammals = [0, 1, 2, 0]

# plot
plt.figure(figsize=(10,7))
plt.stackplot(depth_labels, plankton, fish, cephalopods, corals, mammals, labels=['Plankton','Fish','Cephalopods','Corals','Mammals'], alpha=0.8)
plt.legend(loc='upper right')
plt.title('Evolution of marine life at different ocean depths over the ages')
plt.xlabel('Ocean Depths')
plt.ylabel('Percentage Distribution of Marine Life Forms')

# Set the edge linewidth of the filled area that contains the center point of the bounding box to 1.2257 and change its color to #80da6d
plt.fill_betweenx([40], [0], [40], color='black', edgecolor='black', linewidth=1.2257)

plt.tight_layout()
plt.savefig("figure.png")