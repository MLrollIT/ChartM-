from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Year,Pop,Rock,Country,Hip Hop
2010,100,150,50,70
2011,85,130,55,80
2012,90,120,60,75
2013,70,140,70,85
2014,90,110,60,95
2015,80,150,55,90
2016,70,130,65,110
2017,85,120,70,100
2018,100,150,75,95
2019,95,130,80,105
2020,70,110,85,120
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Pop'].values, df['Rock'].values, df['Country'].values, df['Hip Hop'].values]
labels = ['Pop', 'Rock', 'Country', 'Hip Hop']
# New color scheme
colors = ['#556270', '#4ECDC4', '#C7F464', '#FF6B6B']  # Adjusted colors

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Set background color
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Music Genres Popularity Over The Years')
ax.set_xlabel('Music Genres')
ax.set_ylabel('Popularity')

# Add grid
ax.grid(True, linestyle='--')

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")