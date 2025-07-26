from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dataframe from given data
data = {"Age Group": ["18-25", "26-35", "36-45", "46-55", "56-65"],
        "Gym Visits": [12, 27, 45, 60, 30],
        "Outdoor Activities": [35, 30, 25, 15, 5]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Plot the data
scatter1 = ax.scatter(df["Age Group"], df["Gym Visits"], label='Gym Visits', linestyle='-', marker='o', color='r')
scatter2 = ax.scatter(df["Age Group"], df["Outdoor Activities"], label='Outdoor Activities', linestyle='--', marker='x', color='b')

# Annotation with increased font size
annotation_font_size = 12  # New font size for annotations
for i, txt in enumerate(df["Gym Visits"]):
    ax.annotate(txt, (df["Age Group"][i], df["Gym Visits"][i]), fontsize=annotation_font_size)
for i, txt in enumerate(df["Outdoor Activities"]):
    ax.annotate(txt, (df["Age Group"][i], df["Outdoor Activities"][i]), fontsize=annotation_font_size)

# Labels and title with increased font size
label_title_font_size = 14  # New font size for labels and title
ax.set_xlabel('Age Group', fontsize=label_title_font_size)
ax.set_ylabel('Number of Activities', fontsize=label_title_font_size)
ax.set_title('Number of Activities by Age Group', fontsize=label_title_font_size)

# Adding grid and changing background color
ax.grid(True)
ax.set_facecolor('lightgrey')

# Add legend
ax.legend()

plt.tight_layout()
plt.savefig("myplot.png")