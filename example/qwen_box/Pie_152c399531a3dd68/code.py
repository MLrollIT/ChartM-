from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Provided data
data = {"Factors": ["Accessibility", "Cost Efficiency", "Flexibility", "Student Engagement", "Self-paced Learning", "Improved Technical Skills", "Others"],
        "Percentage": [15, 20, 25, 10, 15, 10, 5]}

labels = data["Factors"]
sizes = data["Percentage"]

fig, ax = plt.subplots()

# Additional parameters
explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Accessibility')

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Setting title, labels and legend
plt.title("Factors Influencing Online Learning") # Add title
plt.legend(labels, title="Factors", loc="upper right") # Add legend

# Setting face color to gray
fig.patch.set_facecolor('gray')

# Modify the slice that contains the center point of the bounding box
slice_index = labels.index("Cost Efficiency")
slice_data = sizes[slice_index]
slice_color = labels[slice_index]
slice_label = labels[slice_index]
slice_explode = [0.1, 0, 0, 0, 0, 0, 0]
slice_autopct = '%1.1f%%'
slice_shadow = True
slice_startangle = 90

# Apply stroke to the slice
slice_stroke_width = 2.74
slice_stroke_color = '#228dd6'

# Modify the slice
ax.pie([slice_data], explode=slice_explode, labels=[slice_label], autopct=slice_autopct, shadow=slice_shadow, startangle=slice_startangle, colors=[slice_color], wedgeprops=dict(width=slice_stroke_width, edgecolor=slice_stroke_color))

plt.tight_layout()
plt.savefig("myplot.png")