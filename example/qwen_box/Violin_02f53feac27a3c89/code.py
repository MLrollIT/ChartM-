import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = [spiral_arm_a, nebula_fields, galactic_core]

# Create a figure and axis
fig, ax = plt.subplots()

# Create a violin plot
sns.violinplot(data=data, ax=ax)

# Set the y-axis label
ax.set_ylabel('Density (Clusters per Square Parsec)')

# Customizing the x-axis labels
ax.set_xticklabels(['Spiral Arm A', 'Nebula Fields', 'Galactic Core'])

# Set the title
ax.set_title('Galactic Cluster Density Mapping')

# Set the animated state of the violins that contain the center point of the bounding box to False
violins = ax.findobj(sns.axes_style('whitegrid'))
for violin in violins:
    if 'center' in violin.get_label():
        violin.set_animated(False)

# Set the clipping state of those violins to False as well
for violin in violins:
    if 'center' in violin.get_label():
        violin.set_clip_on(False)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")