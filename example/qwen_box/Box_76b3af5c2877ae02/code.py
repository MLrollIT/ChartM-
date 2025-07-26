from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Allergies,Year1,Year2,Year3,Year4
Peanuts,100,80,75,150
Dairy,50,45,50,45
Gluten,80,75,70,72
Shellfish,70,65,40,41
Pollen,100,50,60,110
Mold,90,95,110,80
Dust Mites,70,60,80,70
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Year1'].values, df['Year2'].values, df['Year3'].values, df['Year4'].values]
labels = ['Year1', 'Year2', 'Year3', 'Year4']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('white')  # Change background to white

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Allergy Cases Over The Years')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Cases')

# Remove grid
ax.grid(False)  # Remove grid lines

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")