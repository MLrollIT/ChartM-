from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Given Data
data = StringIO("""
Vehicle Type,2010,2015,2020
Sedans,50000,60000,35000
SUVs,40000,35000,70000
Electric Vehicles,500,1500,5000
Trucks,70000,65000,67000
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['2010'].values, df['2015'].values, df['2020'].values]
labels = ['2010', '2015', '2020']
colors = ['#e6194B', '#f58231', '#3cb44b', '#4363d8']  # Updated color scheme

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

# Apply new colors to the boxplot patches
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(colors[i % len(colors)])  # Use modulo to cycle through new colors

# Set title and labels
ax.set_title('Vehicle Sales Over The Years')
ax.set_xlabel('Year')
ax.set_ylabel('Sales')

# Add grid
ax.grid(True)

# Add legend with updated color scheme
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], ['Sedans', 'SUVs', 'Electric Vehicles', 'Trucks'], loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")