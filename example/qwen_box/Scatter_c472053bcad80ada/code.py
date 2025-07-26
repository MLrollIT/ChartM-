from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating the DataFrame from given data
data = {"Platform": ["Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn", "Pinterest", "Reddit", "WeChat", "WhatsApp"],
        "2016": [100, 80, 90, 70, 60, 50, 30, 20, 10],
        "2017": [120, 110, 70, 100, 80, 75, 60, 40, 5],
        "2018": [85, 130, 95, 70, 85, 55, 65, 45, 30]}
df = pd.DataFrame(data)

# Plotting the scatter chart
fig, ax = plt.subplots()

# Adding grids
ax.grid(True)

# Changing the background color
ax.set_facecolor('lightgray')

# Plotting the data for each year
for year in ["2016", "2017", "2018"]:
    ax.scatter(df["Platform"], df[year], marker='o', alpha=0.5, label=year)

    # Annotating data values
    for i, txt in enumerate(df[year]):
        ax.annotate(txt, (df["Platform"][i], df[year][i]))

# Setting the title, labels, and legend
ax.set_title('Platform Usage Over Years')
ax.set_xlabel('Platform')
ax.set_ylabel('Usage')
ax.legend()

# Adjusting the transparency of the scatter points that share the same legend as those containing the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox_points = [bbox.get_x(), bbox.get_y(), bbox.get_width(), bbox.get_height()]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.