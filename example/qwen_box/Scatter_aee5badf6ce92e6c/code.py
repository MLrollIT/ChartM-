from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {
    "Year": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    "Sparrow": [2000, 2100, 2150, 7000, 2200, 2250, 2300, 2350, 2400],
    "Hummingbird": [1000, 3500, 3700, 4000, 4100, 8000, 4200, 4300, 4400],
    "Eagle": [500, 450, 400, 350, 300, 250, 200, 150, 100]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.scatter(df["Year"], df["Sparrow"], label='Sparrow', marker='o', color='red')
ax.scatter(df["Year"], df["Hummingbird"], label='Hummingbird', marker='x', color='green')
ax.scatter(df["Year"], df["Eagle"], label='Eagle', marker='^', color='blue')

# annotate each line at the end of the line with the corresponding legend label
for i, txt in enumerate(df["Sparrow"]):
    ax.annotate(txt, (df["Year"][i], df["Sparrow"][i]))
for i, txt in enumerate(df["Hummingbird"]):
    ax.annotate(txt, (df["Year"][i], df["Hummingbird"][i]))
for i, txt in enumerate(df["Eagle"]):
    ax.annotate(txt, (df["Year"][i], df["Eagle"][i]))

ax.set_title('Birds population over the years')
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.grid(True)
ax.set_facecolor('lightgray')
ax.legend()

# Modify the transparency of the scatter points that share the same legend as those containing the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox_points = [bbox.get_x(), bbox.get_y(), bbox.get_width(), bbox.get_height()]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points[3] + 0.05]
bbox_points = [bbox_points[0] - 0.05, bbox_points[1] - 0.05, bbox_points[2] + 0.05, bbox_points