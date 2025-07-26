import matplotlib.pyplot as plt
import numpy as np

# Given data
activities = ['Studying', 'Working', 'Socializing', 'Exercising', 'Leisure Activities']
percentage_distribution = [20, 30, 15, 10, 25]

# Make the data suitable for a step plot
x = np.concatenate([[i, i+1] for i in range(len(activities))])
y = np.repeat(percentage_distribution, 2)

# Plot
plt.figure(figsize=(10,6))
plt.step(x, y, where='post')

# labeling
plt.xticks(range(len(activities)), activities)
plt.yticks(np.arange(0, max(percentage_distribution)+10, step=10))
plt.xlabel('Activities')
plt.ylabel('Percentage Distribution (%)')
plt.title('Time Spent on Daily Activities for Individuals Aged 18-24')

# Set the clipping state of the steps that contain the center point of the bounding box to True
plt.gca().set_clip_path(plt.gca().patch)

plt.tight_layout()
plt.savefig("figure.png")