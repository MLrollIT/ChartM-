from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Load the data
data = pd.DataFrame({
    "Culture": ["American", "Chinese", "Indian", "Japanese", "Mexican", "French"],
    "Vegetarian": [45, 50, 80, 60, 50, 40],
    "Seafood": [60, 92, 40, 95, 70, 80],
    "Fast Food": [85, 74, 50, 55, 65, 70]
})

fig, ax = plt.subplots()

# Plot each dietary preference as a scatter plot
for column in ["Vegetarian", "Seafood", "Fast Food"]:
    ax.scatter(data["Culture"], data[column], label=column, marker='o')

# Annotate each point with its corresponding value
for i, txt in enumerate(data["Vegetarian"]):
    ax.annotate(txt, (data["Culture"][i], txt))
for i, txt in enumerate(data["Seafood"]):
    ax.annotate(txt, (data["Culture"][i], txt))
for i, txt in enumerate(data["Fast Food"]):
    ax.annotate(txt, (data["Culture"][i], txt))

ax.set_xlabel('Culture', fontsize=15)
ax.set_ylabel('Preference (%)', fontsize=15)
ax.set_title('Food preferences by culture')
ax.legend()

ax.grid(True)
ax.set_facecolor('lightgray')

# Update the edge color and width of the scatter points that share the same legend as those containing the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), which="center")
bbox_points = [bbox.get_x(), bbox.get_y(), bbox.get_width(), bbox.get_height()]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 1]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 == 0]
bbox_points = [bbox_points[i] for i in range(4) if i % 2 ==