import matplotlib.pyplot as plt

Regions = ['Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5']

# Data points
Minor = [8, 10, 5, 12, 7]
Light = [12, 15, 10, 18, 11]
Moderate = [5, 8, 3, 10, 6]
Strong = [1, 2, 1, 4, 2]

fig, ax = plt.subplots()

ax.stackplot(Regions, Minor, Light, Moderate, Strong, labels=['Minor','Light','Moderate','Strong'])
ax.legend(loc='upper left')
ax.set_title('Distribution of Earthquake Intensities across Different Regions')
ax.set_xlabel('Regions')
ax.set_ylabel('Number of Earthquakes')

bbox = ax.bbox_to_anchor([0.2, 0.2, 0.3, 0.3])
bbox_patch = plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], fc='none', ec='black', lw=2)
ax.add_patch(bbox_patch)

ax.set_xlim(0, 5)
ax.set_ylim(0, 40)

plt.tight_layout()
plt.savefig("figure.png")