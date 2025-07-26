import matplotlib.pyplot as plt
import seaborn as sns

# Prepare the bond lengths data
Stellarite_lengths = [135, 140, 138, 142, 137, 139, 136, 141]
Celestene_lengths = [132, 136, 134, 137, 131, 135, 133, 139]
Nebulon_lengths = [130, 133, 128, 135, 131, 137, 129, 136]

# Pack all bond lengths into a single list
all_lengths = Stellarite_lengths + Celestene_lengths + Nebulon_lengths

# Create labels for each bond length
all_labels = ['Stellarite']*len(Stellarite_lengths) + ['Celestene']*len(Celestene_lengths) + ['Nebulon']*len(Nebulon_lengths)

# Create violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x=all_labels, y=all_lengths)

# Add title and labels
plt.title('Carbon-Carbon Bond Lengths of Interstellar Compounds')
plt.xlabel('Compounds')
plt.ylabel('Bond Lengths (pm)')

# Modify the linewidth of the edges of the violins that contain the center point of the bounding box to 2.6
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], bbox[1] + bbox[3]]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=2.6, edgecolor='black', facecolor='none'))

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")