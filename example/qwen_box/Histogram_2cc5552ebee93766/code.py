import matplotlib.pyplot as plt

# Data
current_speeds = [0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.3, 2.6, 2.9, 3.2, 3.5, 3.8, 4.1, 4.4, 4.7, 5.0, 5.3, 5.6, 5.9, 6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8.0]

plt.hist(current_speeds, bins=20, edgecolor='black') # You can adjust the number of bins as you deem fit

plt.title('Histogram of Ocean Current Speeds')
plt.xlabel('Speed (m/s)')
plt.ylabel('Frequency')

# Add a shadow effect to the bars that include the center point of the bounding box
bbox = (2.43, 3.09)
shadow_color = 'gold'
alpha = 0.87

# Get the current patches
patches = plt.gca().patches

# Iterate over the patches and modify the shadow effect
for patch in patches:
    if patch.get_bbox().contains(bbox):
        patch.set_facecolor('gold')
        patch.set_alpha(alpha)
        patch.set_edgecolor('black')
        patch.set_zorder(2)

plt.tight_layout()
plt.savefig("Edit_figure.png")