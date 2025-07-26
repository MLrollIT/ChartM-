from io import StringIO
import numpy as np

from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = StringIO("""
Profession,Hours_per_week,Type_of_exercise
Doctor,15,Yoga
Engineer,8,Weightlifting
Teacher,20,Running
""")

# Read the data into a pandas DataFrame
df = pd.read_csv(data)

# Sort the data by Hours_per_week
df = df.sort_values("Hours_per_week")

y = np.arange(len(df.Profession))  # the label locations
height = 0.6  # the height of the bars

fig, ax = plt.subplots()

# Create the bar chart
bars = ax.barh(y, df.Hours_per_week, height, color='skyblue', edgecolor='blue')

# Add some text for labels, title and custom y-axis tick labels, etc.
ax.set_xlabel('Hours per Week')
ax.set_title('Exercise Habits by Profession')
ax.set_yticks(y)
ax.set_yticklabels(df.Profession)
ax.grid(visible=True)
ax.set_facecolor('lightgray')

# Add bar labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 5 points horizontal offset
                textcoords="offset points",
                ha='left', va='center')

# Invert the y-axis so the professions read top-to-bottom
ax.invert_yaxis()

# Add a shadow effect to the bars that contain the center point of the bounding box
bbox = plt.Bbox([[135, 24], [135 + 807, 24 + 574]])
for bar in bars:
    if bar.get_x() + bar.get_width() / 2 in df.Hours_per_week.values:
        bar.set_facecolor('gold')
        bar.set_edgecolor('gold')
        bar.set_zorder(2)
        bar.set_clip_box(bbox)

plt.tight_layout()
plt.savefig("myplot.png")