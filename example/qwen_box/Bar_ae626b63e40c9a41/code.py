from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# given data
data = """Demographics,Recycling Habits
Teenagers,60
Young Adults,75
Middle-aged Adults,90
Elderly,50
Teenagers,100
Young Adults,45
Middle-aged Adults,70
Elderly,30"""

# convert data to pandas dataframe
df = pd.read_csv(StringIO(data))

# calculate average recycling habits for each demographic
df = df.groupby("Demographics").mean().reset_index()

# set demographics and recycling habits
demographics = df["Demographics"].tolist()
recycling_habits = df["Recycling Habits"].tolist()

x = np.arange(len(demographics))  # the label locations
width = 0.5  # the width of the bars

fig, ax = plt.subplots(figsize=(8, 6))

bars = ax.bar(x, recycling_habits, width, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Recycling Habits Score')
ax.set_title('Average Recycling Habits by Demographic')
ax.set_xticks(x)
ax.set_xticklabels(demographics)
ax.bar_label(bars, padding=3)

# Setting background color and grid
ax.set_facecolor('gray')
ax.grid(True)

# Set the picker state of the bars that contain the center point of the bounding box to False
for bar in bars:
    if bar.contains((0.5, 0.5)):
        bar.set_picker(True)
        bar.set_visible(False)

plt.tight_layout()
plt.savefig("myplot.png")