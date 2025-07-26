from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Age Group,Vegetarian Diet,Paleo Diet,Keto Diet
Young Adults (18-29),50,70,90
Middle Aged (30-49),60,80,65
Seniors (50+),45,62,70
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Vegetarian Diet'].values, df['Paleo Diet'].values, df['Keto Diet'].values]
labels = ['Vegetarian Diet', 'Paleo Diet', 'Keto Diet']
colors = ['#e377c2', '#7f7f7f', '#bcbd22']  # Updated colors

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Diet Popularity by Age Group')
ax.set_xlabel('Diet Type')
ax.set_ylabel('Popularity')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")