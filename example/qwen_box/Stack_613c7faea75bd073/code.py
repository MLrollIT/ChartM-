import matplotlib.pyplot as plt

# Time intervals
time = [1, 2, 3, 4, 5]

# Tumor sizes
group_A = [10, 15, 20, 25, 30]
group_B = [12, 18, 22, 28, 35]
group_C = [8, 14, 19, 23, 29]

fig, ax = plt.subplots()

ax.stackplot(time, group_A, group_B, group_C, labels=['Group A', 'Group B', 'Group C'])
ax.legend(loc='upper left')

plt.xlabel('Time Intervals')
plt.ylabel('Tumor Size (in mm)')
plt.title('Tumor Growth Progression in Different Treatment Groups')

# Change the hatch pattern of the areas that contain the center point of the bounding box to '|'
bbox = ax.bbox_to_anchor([0.35, 0.35, 0.45, 0.45])
ax.add_patch(plt.Rectangle((0.35, 0.35), 0.1, 0.1, fill=True, hatch='|', ec='none', fc='none', zorder=100))

plt.tight_layout()
plt.savefig("figure.png")