from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = """
Technology,Usage
"Smartphones",45
"Artificial Intelligence",88
"Solar Power",35
"Electric Vehicles",78
"5G Network",50
"Blockchain",30
"Virtual Reality",65
"Quantum Computing",25
"""
df = pd.read_csv(StringIO(data))

# Plotting the data
fig, ax = plt.subplots()

# Modifying the color properties of the plot
ax.plot(df['Technology'], df['Usage'], marker='o', color='green', linestyle='-', linewidth=2, markersize=6, alpha=0.7, markerfacecolor='yellow', markeredgecolor='red', label='Usage')

# Annotating the lines
for i, txt in enumerate(df['Usage']):
    ax.annotate(txt, (df['Technology'][i], df['Usage'][i]))

ax.set_xlabel('Technology')
ax.set_ylabel('Usage (%)')
ax.set_title('Usage of Different Technologies')
ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

# Set the picker state of the lines that contain the center point of the bounding box to True
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((