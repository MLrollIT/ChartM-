from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

data = {'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007],
        'Climate Change Effects': [0.4, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 2.0],
        'Greenhouse Gas Emissions': [1.2, 1.1, 0.9, 0.5, 0.4, 0.3, 0.2, 1.5],
        'Global Average Temperature': [0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 1.0]}

labels = ['Climate Change Effects', 'Greenhouse Gas Emissions', 'Global Average Temperature']

heatmap_data = np.array([data[label] for label in labels])

fig, ax = plt.subplots()
cax = ax.imshow(heatmap_data, cmap='viridis', alpha=0.7)
ax.set_xticks(np.arange(len(data['Year'])))
ax.set_yticks(np.arange(len(labels)))
ax.set_xticklabels(data['Year'])
ax.set_yticklabels(labels)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(labels)):
    for j in range(len(data['Year'])):
        if heatmap_data[i, j] == 0.65:
            text = ax.text(j, i, heatmap_data[i, j], ha="center", va="center", color="w", edgecolor="#ee5806")
        else:
            text = ax.text(j, i, heatmap_data[i, j], ha="center", va="center", color="w")

fig.colorbar(cax, ax=ax, orientation='vertical')
ax.set_title("Climate Change Data Over Years")
ax.set_xlabel('Year')
ax.set_ylabel('Metrics')
ax.grid(True)
fig.tight_layout()
plt.savefig("myplot.png")