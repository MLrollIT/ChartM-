import matplotlib.pyplot as plt

# Data
phases = ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4']
tremors = [15, 0, 0, 0]
ash = [0, 25, 0, 0]
lava = [0, 0, 20, 0]
pyroclastic = [0, 0, 0, 30]

# Create stack plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(phases, tremors, ash, lava, pyroclastic, labels=['Initial Tremors', 'Ash Emissions', 'Lava Flow', 'Pyroclastic Flow'])

# Add legend and labels
ax.legend(loc='upper left')
ax.set_xlabel('Volcanic Phases')
ax.set_ylabel('Number of Eruptions')
ax.set_title('Volcano Eruption Simulation - Eruption Intensity Levels')

# Adjust transparency and hatch pattern of fill areas containing the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox_points = bbox.get_points()
bbox_points[0] = (bbox_points[0][0], 0.6379)
bbox_points[1] = (bbox_points[1][0], 0.6379)
bbox.set_points(bbox_points)
bbox.set_hatch('/')
bbox.set_clip_on(True)

# Save figure
plt.tight_layout()
plt.savefig("figure.png")