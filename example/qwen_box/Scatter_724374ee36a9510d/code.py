from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Prepare data
data = {
    "Time Period": ["Morning", "Afternoon", "Evening", "Night", "Early Morning", "Late Night", "Midnight"],
    "App Usage": [120, 80, 150, 90, 70, 200, 50],
    "Call Duration": [15, 20, 25, 10, 5, 30, 8],
    "Data Consumption": [2.5, 3.0, 2.0, 1.5, 1.0, 3.5, 1.2]
}

df = pd.DataFrame(data)

# Set up the figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.scatter(df["Time Period"], df["App Usage"], label='App Usage', marker='o', color='r')
ax.scatter(df["Time Period"], df["Call Duration"], label='Call Duration', marker='v', color='g')
ax.scatter(df["Time Period"], df["Data Consumption"], label='Data Consumption', marker='s', color='b')

# Set the title and labels
ax.set_title('App usage, Call duration and Data Consumption over different time periods', fontsize=15)
ax.set_xlabel('Time Period', fontsize=12)
ax.set_ylabel('Values', fontsize=12)

# Remove grid and set background color to white
ax.grid(False)
ax.set_facecolor('white') # Change background color here

# Add legend
ax.legend()

# Annotate data points
for i, txt in enumerate(df["App Usage"]):
    ax.annotate(txt, (df["Time Period"][i], df["App Usage"][i]))
for i, txt in enumerate(df["Call Duration"]):
    ax.annotate(txt, (df["Time Period"][i], df["Call Duration"][i]))
for i, txt in enumerate(df["Data Consumption"]):
    ax.annotate(txt, (df["Time Period"][i], df["Data Consumption"][i]))

# Change the shape of the points that share the same legend as those containing the center point of the bounding box to a 'triangle'
ax.scatter(df["Time Period"][3], df["App Usage"][3], label='App Usage', marker='^', color='r', alpha=0.5)
ax.scatter(df["Time Period"][3], df["Call Duration"][3], label='Call Duration', marker='^', color='g', alpha=0.5)
ax.scatter(df["Time Period"][3], df["Data Consumption"][3], label='Data Consumption', marker='^', color='b', alpha=0.5)

# Add a shadow effect to these points with a 6.0 pixel offset and a silver color
ax.scatter(df["Time Period"][3], df["App Usage"][3], label='App Usage', marker='^', color='r', alpha=0.5, shadow=True, offset=6.0, facecolor='silver')
ax.scatter(df["Time Period"][3], df["Call Duration"][3], label='Call Duration', marker='^', color='g', alpha=0.5, shadow=True, offset=6.0, facecolor='silver')
ax.scatter(df["Time Period"][3], df["Data Consumption"][3], label='Data Consumption', marker='^', color='b', alpha=0.5, shadow=True, offset=6.0, facecolor='silver')

plt.tight_layout()
plt.savefig("myplot.png")