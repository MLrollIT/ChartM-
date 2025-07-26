# Required Libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Dataset
systolic_bp = [120, 122, 118, 125, 130, 132, 128, 134, 120, 115, 136, 128, 126, 124, 127, 130, 133, 129, 126, 122]
diastolic_bp = [80, 85, 82, 90, 88, 86, 85, 92, 81, 79, 88, 84, 86, 83, 84, 89, 90, 87, 85, 82]
labels = ['Systolic']*len(systolic_bp) + ['Diastolic']*len(diastolic_bp)
values = systolic_bp + diastolic_bp

data = pd.DataFrame({'Blood Pressure Type': labels, 'Value (mmHg)': values})

# Violin plot 
plt.figure(figsize=(10,6))
sns.violinplot(x='Blood Pressure Type', y='Value (mmHg)', data=data)
plt.title('Blood Pressure Distribution')
plt.tight_layout()

# Set the clipping box for the violins that contain the center point of the bounding box
bbox = plt.bbox_to_transform(plt.gca().bbox)
bbox = bbox.transformed(matplotlib.transforms.Bbox.from_extents(21, 272, 504, 223))

# Enable the animated state for these violins
plt.violinplot(x='Blood Pressure Type', y='Value (mmHg)', data=data, clip_on=False, widths=0.5, showmeans=True, showextrema=False, showmedians=False, bw_method='scott', cut=1, clip=bbox, animated=True)

plt.savefig("Edit_figure.png")