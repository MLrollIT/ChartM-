import matplotlib.pyplot as plt
import numpy as np

# Your data
activity_levels = ['0-1 days', '2-3 days', '4-5 days', '6-7 days']
scores = [70, 75, 80, 85]

# Plotting
plt.figure(figsize=(10,5))
plt.plot(activity_levels, scores, marker = 'o', drawstyle = 'steps-post')
plt.title('Impact of physical activity on academic performance')
plt.xlabel('Physical Activity [days per week]')
plt.ylabel('Academic Score')
plt.ylim(65, 90)  # This adds some space below and above the bars
plt.tight_layout()
plt.savefig("figure.png")

# Get the center point of the bounding box
bbox = plt.gca().bbox
center = bbox.get_width() / 2, bbox.get_height() / 2

# Find the index of the center point
center_index = np.argmax(np.abs(np.array(scores) - center))

# Modify the rasterized state of the steps that contain the center point
plt.plot(activity_levels, scores, marker = 'o', drawstyle = 'steps-post', rasterized = False)

plt.title('Impact of physical activity on academic performance')
plt.xlabel('Physical Activity [days per week]')
plt.ylabel('Academic Score')
plt.ylim(65, 90)  # This adds some space below and above the bars
plt.tight_layout()
plt.savefig("Edit_figure.png")