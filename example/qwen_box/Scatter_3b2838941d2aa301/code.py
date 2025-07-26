from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'North America': [12.7, 13.5, 14.2, 15.0, 16.1, 14.8, 15.5],
    'Europe': [15.6, 16.2, 17.1, 18.0, 20.0, 19.8, 22.0],
    'Asia': [18.9, 22.3, 20.8, 23.5, 18.0, 25.5, 24.0]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Draw scatter plots
for column in df.columns[1:]:
    ax.scatter(df['Year'], df[column], label=column)

# Set chart title and labels
ax.set_title('Scatter Chart of Data over Years', fontsize=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Value', fontsize=12)

# Set grid lines and background color
ax.grid(False)  # Disable grid lines
ax.set_facecolor('white')  # Change background color to white

# Set legend
ax.legend()

# Annotate each line with the label
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Adjust the transparency of the scatter points that share the same legend as those containing the center point of the bounding box to 0.59
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox_points = [bbox.x0, bbox.y0, bbox.width, bbox.height]
bbox_points = [bbox_points[i] * 0.59 for i in range(4)]
bbox = ax.bbox_to_anchor(*bbox_points, transform=ax.transAxes)
ax.add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], facecolor='none', edgecolor='silver', linewidth=5.8))

# Set the file name for the saved figure
plt.savefig("myplot_no_grid_white_background.png")