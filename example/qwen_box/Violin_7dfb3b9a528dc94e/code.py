import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Defining the data
emotions = ['Bliss', 'Confusion', 'Fear', 'Nostalgia', 'Serenity']
values = [[4, 4, 3, 5, 4, 3, 5, 4],
          [2, 3, 2, 4, 3, 3, 2, 4],
          [5, 4, 5, 3, 4, 5, 3, 4],
          [3, 2, 4, 3, 2, 3, 4, 3],
          [4, 5, 3, 4, 5, 4, 3, 5]]

# Preparing data for the plot
data = pd.DataFrame(dict(zip(emotions, values)))

# Melting the dataframe
data_melted = data.melt(var_name='Emotion', value_name='Intensity')

# Creating the violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Emotion', y='Intensity', data=data_melted)
plt.title("Emotions intensity in Dreamscapes")

# Change the color of the violins that contain the center point of the bounding box to #c6262f
# Set their z-order to 7
# Apply a shadow effect to these violins with an offset of (2.58, 2.72), using a shadow color randomly selected from ['gray', 'gold']
bbox = plt.gca().get_position()
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.get_points()
bbox[0] += (2.58, 2.72)
bbox[1] += (2.58, 2.72)
bbox = bbox.tolist()
plt.gca().add_patch(plt.Rectangle((bbox[0][0], bbox[0][1]), bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1], fill=False, edgecolor='black', zorder=7))
plt.gca().add_patch(plt.Rectangle((bbox[0][0], bbox[0][1]), bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1], fill=False, edgecolor='black', zorder=7, alpha=0.5, shadow=True, offset=(2.58, 2.72), color=random.choice(['gray', 'gold'])))

plt.tight_layout()
plt.savefig("figure.png")