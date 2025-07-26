import pandas as pd
# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
random_movement = [2.5, 3.0, 2.7, 3.2, 2.8, 3.4, 3.1, 2.9, 2.6, 3.3]
circular_path = [4.5, 4.0, 4.2, 4.8, 4.1, 4.9, 4.6, 4.3, 4.7, 4.4]
targeted_navigation = [5.5, 5.3, 5.1, 5.7, 5.4, 5.6, 5.9, 5.2, 5.8, 5.0]

# Combine all the data and labels
data = [random_movement, circular_path, targeted_navigation]
labels = ['Random Movement', 'Circular Path', 'Targeted Navigation']

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=data)

# Set the x ticks and labels
plt.xticks([0, 1, 2], labels)

# Add title & labels
plt.title('Robot Speed Distributions under Different Experimental Conditions')
plt.xlabel('Experimental Condition')
plt.ylabel('Speed (cm/s)')

# Modify the transparency of the lines in the violin that contains the center point of the bounding box
violin = plt.gca().violinplot(data, labels=labels, showmeans=True, showextrema=False, showmedians=False)
violin['bodies'][1].set_alpha(0.42)
violin['bodies'][1].set_visible(False)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")