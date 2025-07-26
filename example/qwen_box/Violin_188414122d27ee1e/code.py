import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
    'Topsoil Layer': {
        'Location 1': [16.5, 17.0, 18.2, 16.8, 17.5, 17.3, 17.9, 16.7, 17.8, 16.1],
        'Location 2': [15.8, 16.2, 17.0, 16.5, 17.2, 16.7, 16.9, 16.3, 17.1, 15.9],
        'Location 3': [17.1, 17.5, 18.0, 17.2, 17.9, 18.4, 17.8, 17.3, 17.6, 16.9]
    },
    'Subsoil Layer': {
        'Location 1': [14.3, 14.8, 15.2, 14.5, 15.0, 14.7, 14.9, 14.3, 15.1, 14.6],
        'Location 2': [13.6, 14.0, 14.5, 13.8, 14.3, 14.1, 14.2, 13.7, 14.4, 13.9],
        'Location 3': [15.0, 15.5, 16.0, 15.3, 15.8, 15.6, 15.9, 15.1, 15.7, 15.2]
    },
    'Bedrock Layer': {
        'Location 1': [12.5, 12.8, 13.1, 12.7, 13.0, 12.9, 13.2, 12.6, 13.3, 12.4],
        'Location 2': [11.8, 12.2, 12.6, 12.0, 12.5, 12.3, 12.4, 12.1, 12.7, 12.0],
        'Location 3': [13.0, 13.5, 13.9, 13.2, 13.7, 13.6, 13.8, 13.3, 13.8, 13.1]
    }
}

# Processing data to be in a suitable form for the violin plot
labels, temps = [], []
for layer, locations in data.items():
    for location, temperatures in locations.items():
        labels.append(f'{layer}\n{location}')
        temps.append(temperatures)

# Plot
plt.figure(figsize=(10, 8))
sns.set(style="whitegrid")
sns.violinplot(data=temps, palette="Pastel1", inner="stick", scale="count")
plt.title('Surface Heat Distribution Analysis')
plt.ylabel('Temperature (°C)')
plt.xticks(range(len(labels)), labels)

# Change the label of the violin that contain the center point of the bounding box to 'A new Label'
violin = plt.gca().violinplots()[0]
violin['bodies'][0].set_label('A new Label')

# Set the picker state of the same violin to False
violin = plt.gca().violinplots()[0]
violin['bodies'][0].set_picker(False)

plt.tight_layout()
plt.savefig("figure.png")