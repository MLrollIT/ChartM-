# Necessary Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Data
EST = [50.2, 48.9, 52.5, 58.1, 64.3, 70.2, 73.6, 75.8, 76.5, 75.2, 69.5, 60.7]
GMT = [47.6, 49.1, 50.3, 51.2, 52.1, 53.5, 54.8, 56.2, 57.3, 58.4, 58.1, 56.9]
JST = [45.3, 46.1, 47.9, 49.6, 51.1, 52.4, 53.6, 54.9, 56.2, 57.5, 58.9, 60.3]
AEST = [43.8, 44.2, 45.9, 47.8, 50.1, 52.5, 55.0, 57.4, 59.6, 61.3, 61.9, 61.4]
PST = [48.0, 50.1, 52.3, 55.0, 58.1, 61.4, 64.3, 66.0, 66.5, 65.9, 63.7, 60.3]

# Combine Data
data = [EST, GMT, JST, AEST, PST]
timezone = ['EST', 'GMT', 'JST', 'AEST', 'PST']

# Create the violin plot
plt.figure(figsize=(10,6))
sns.violinplot(data=data)
plt.xticks([0, 1, 2, 3, 4], timezone)
plt.title('Energy Consumption by Time Zone')
plt.xlabel('Time Zone')
plt.ylabel('Energy Consumption (kWh)')
plt.tight_layout()

# Add a dashed outline around the violins enclosed by the bounding box
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], bbox[1] + bbox[3]]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], fill=False, edgecolor='#b9b37b', linewidth=1.73, linestyle='dashed'))

plt.savefig("figure.png")