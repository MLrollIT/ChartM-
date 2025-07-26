from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Year,Climate Change Effects,Greenhouse Gas Emissions,Global Average Temperature
2000,0.4,1.2,0.6
2001,0.5,1.1,0.65
2002,0.55,0.9,0.7
2003,0.6,0.5,0.75
2004,0.65,0.4,0.8
2005,0.7,0.3,0.85
2006,0.75,0.2,0.9
2007,2.0,1.5,1.0
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Climate Change Effects'].values, df['Greenhouse Gas Emissions'].values, df['Global Average Temperature'].values]
labels = ['Climate Change Effects', 'Greenhouse Gas Emissions', 'Global Average Temperature']
# Updated color scheme to pastel
colors = ['#92c6ff', '#97f0aa', '#ff9f9a']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Climate Change Indicators Over The Years')
ax.set_xlabel('Indicators')
ax.set_ylabel('Values')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Set the picker state of the boxes that contain the center point of the bounding box to True
for box in bp['boxes']:
    box.set_picker(True)

# Change the z-order of the boxes that contain the center point of the bounding box to 7
for box in bp['boxes']:
    box.set_zorder(7)

# Add a shadow effect with an offset of (3.31, 2.81) to the boxes that contain the center point of the bounding box
for box in bp['boxes']:
    box.set_edgecolor('black')
    box.set_edgealpha(0.5)
    box.set_boxstyle('square', pad=0.3, rounding_size=0.3)
    box.set_facecolor('none')
    box.set_zorder(7)
    box.set_transform(box.get_transform().rotate_deg(90))
    box.set_transform(box.get_transform().translate((3.31, 2.81)))

# Save the figure
plt.tight_layout()
plt.savefig("myplot_pastel.png")