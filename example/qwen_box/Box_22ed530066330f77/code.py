from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = StringIO("""
Year,Book Sales
2005,2000
2006,4000
2007,10000
2008,2500
2009,9000
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Book Sales'].values]
labels = ['Book Sales']
colors = ['#1f77b4']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance and change background to white
ax.set_facecolor('white')  # Changed from '#f0f0f0' to 'white'

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Book Sales Over The Years')
ax.set_xlabel('Year')
ax.set_ylabel('Sales')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")