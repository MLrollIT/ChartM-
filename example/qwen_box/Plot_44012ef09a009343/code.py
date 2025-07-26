from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data
data = '''\
Country,2017,2018,2019
USA,65,70,45
UK,52,50,55
Germany,58,53,59
Australia,45,46,43
Canada,48,43,70
China,90,85,92
India,100,98,105
Brazil,40,38,40
'''

# Create a DataFrame from the data
df = pd.read_csv(StringIO(data))

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
for country in df["Country"]:
    line, = ax.plot(df.columns[1:], df[df["Country"] == country].values[0][1:], linestyle='-', linewidth=2, marker='o', markersize=10, alpha=0.7)

# Set the title and labels
ax.set_title('Country Yearly Data')
ax.set_xlabel('Year')
ax.set_ylabel('Value')

# Add a legend
ax.legend(df["Country"])

# Annotate each line at the end
for line, name in zip(ax.lines, df["Country"]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Add grid
ax.grid(True)

# Change the background color
ax.set_facecolor('lightgray')

# Change the marker face color of the lines that contain the center point of the bounding box to #cf3d85
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5),