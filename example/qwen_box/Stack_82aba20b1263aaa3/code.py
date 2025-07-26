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

bbox = plt.Bbox([[77, 181], [77 + 952, 181 + 710]])
ax.set_clip_box(bbox)
ax.set_rasterized(False)

plt.tight_layout()
plt.savefig("figure.png")