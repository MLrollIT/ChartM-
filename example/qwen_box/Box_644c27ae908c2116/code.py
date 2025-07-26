# Importing Necessary Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Data
platforms = {
    'Platform A': [9, 8, 7, 9, 8, 7, 8, 9, 9, 8, 7, 6, 8, 9, 9],
    'Platform B': [10, 9, 9, 8, 10, 9, 9, 10, 10, 9, 8, 9, 8, 7, 7],
    'Platform C': [7, 7, 6, 8, 7, 9, 8, 6, 7, 6, 7, 8, 9, 7, 8],
    'Platform D': [8, 7, 8, 7, 9, 8, 8, 7, 8, 7, 8, 7, 8, 9, 9],
    'Platform E': [9, 10, 9, 10, 8, 9, 9, 10, 9, 10, 9, 10, 10, 9, 9],
    'Platform F': [6, 7, 7, 8, 6, 7, 8, 9, 8, 7, 7, 8, 6, 8, 8]
}

# Preparing data for boxplot
labels, data = platforms.keys(), platforms.values()

# Plotting boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(data, vert=True, patch_artist=True)
plt.xticks(range(1, len(labels) + 1), labels)
plt.title('Comparison of Customer Satisfaction Ratings For Online Shopping Platforms')
plt.xlabel('Online Shopping Platforms')
plt.ylabel('Customer Satisfaction Ratings')
plt.grid()
plt.tight_layout()

# Change the body color of the boxes that contain the center point of the bounding box to #b84de0 and adjust their transparency to 0.41
for box in plt.gca().get_children():
    if isinstance(box, plt.Rectangle):
        box.set_facecolor('#b84de0')
        box.set_alpha(0.41)

plt.savefig("Edit_figure.png")