import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for depths at different regions and coordinates
data = {
    'Region': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Coordinates': ['(10,20)', '(20,30)', '(30,40)', '(40,50)', '(50,60)', '(60,70)'],
    'Depth': [
        [5000, 4900, 5100, 4800, 4950],
        [4800, 4700, 4850, 4750, 4950],
        [5200, 5250, 5100, 5150, 5000],
        [4500, 4600, 4550, 4650, 4700],
        [4700, 4750, 4650, 4850, 4800],
        [4900, 4950, 4850, 5000, 5100]
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Expanding the list of depths into separate rows for each depth measurement
df = df.explode('Depth')
df['Depth'] = pd.to_numeric(df['Depth'])

# Creating the violin plot
plt.figure(figsize=(12, 8))
sns.violinplot(x='Coordinates', y='Depth', hue='Region', data=df, split=True, palette='muted')
plt.title('Ocean Floor Seabed Topography')
plt.xlabel('Coordinates (Latitude, Longitude)')
plt.ylabel('Depth (in meters)')
plt.legend(title='Region')
plt.grid(True)
plt.tight_layout()

# Get the center point of the bounding box
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
center_point = bbox.center

# Find the violin plot that contains the center point of the bounding box
violins = plt.gca().findobj(sns.axisgrid.Violin)
for violin in violins:
    if center_point in violin.get_paths()[0].vertices:
        violin.set_facecolor('#895b92')
        violin.set_alpha(0.76)

plt.savefig("figure.png")