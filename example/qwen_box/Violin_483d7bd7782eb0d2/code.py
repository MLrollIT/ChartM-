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

# Set the picker state of the section that contains the center point of the violin chart to False
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(plt.NullFormatter())
plt.gca().xaxis.set_major_locator(plt.NullLocator())

plt.tight_layout()
plt.savefig("figure.png")