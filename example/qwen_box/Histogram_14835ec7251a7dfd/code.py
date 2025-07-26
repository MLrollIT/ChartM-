import matplotlib.pyplot as plt

# Data points for survival outcomes and counts
survival_outcomes = ['Survived', 'Did not survive']
counts = [342, 549]

# Plotting the histogram
fig, ax = plt.subplots()
ax.bar(survival_outcomes, counts, color=['green','red'])

# Labeling the axes
plt.xlabel('Survival Outcomes')
plt.ylabel('Count')

# Setting the title
plt.title('Survival Rate of Shipwreck Passengers')

# Get the center point of the bounding box
bbox = ax.bbox_to_anchor([0.5, 0.5, 0.3, 0.3])

# Set the animated state of the bars that contain the center point of the bounding box to False
for bar in ax.patches:
    if bar.get_bbox().contains(bbox):
        bar.set_animated(False)

# Set the snap state of the corresponding bars to False as well
for bar in ax.patches:
    if bar.get_bbox().contains(bbox):
        bar.set_snap(False)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")