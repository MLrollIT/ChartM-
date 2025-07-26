from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Define the age groups and diets
age_groups = ["18-25", "25-35", "35-45", "45-55"]
diets = ["Vegan", "Gluten-Free", "Keto"]

# Define the number of people following each diet in each age group
data = np.array([[200, 400, 600],
                 [450, 550, 350],
                 [500, 300, 200],
                 [600, 700, 1000]])

fig, ax = plt.subplots()

# Plot the data as a heatmap with a different colormap
im = ax.imshow(data, cmap='viridis', alpha=0.7)  # Changed colormap to 'viridis'

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(diets)))
ax.set_xticklabels(diets)
ax.set_yticks(np.arange(len(age_groups)))
ax.set_yticklabels(age_groups)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(age_groups)):
    for j in range(len(diets)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

# Add some extra information to the plot
ax.set_title("Number of people following each diet in each age group")
ax.set_xlabel("Diet")
ax.set_ylabel("Age Group")
ax.grid(True)
fig.tight_layout()
ax.set_facecolor('white')  # Changed background to white

# Save the plot
plt.savefig("myplot.png")