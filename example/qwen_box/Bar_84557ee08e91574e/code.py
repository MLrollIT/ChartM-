from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = StringIO("""
Profession,Hours Worked (2019),Hours Worked (2020)
Doctors,65,70
Software Developers,45,42
Teachers,50,38
Truck Drivers,55,60
Lawyers,60,58
Chefs,55,50
""")

df = pd.read_csv(data)

professions = df['Profession'].tolist()
hours_2019 = df['Hours Worked (2019)'].tolist()
hours_2020 = df['Hours Worked (2020)'].tolist()

x = np.arange(len(professions))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

rects1 = ax.bar(x - width/2, hours_2019, width, label='2019', color='#1f77b4', edgecolor='black')
rects2 = ax.bar(x + width/2, hours_2020, width, label='2020', color='#ff7f0e', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Hours Worked')
ax.set_title('Average Hours Worked by Profession')
ax.set_xticks(x)
ax.set_xticklabels(professions)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Setting background color to white and removing grid lines
ax.set_facecolor('white')  # Change to white background
ax.grid(False)  # Remove grid lines

# Change the clipping state of the bars that share the same legend with the bar that contains the center point of the bounding box to False
for i in range(len(professions)):
    if i == 3:
        rects1[i].set_clipping_box(ax.bbox)
        rects2[i].set_clipping_box(ax.bbox)
    else:
        rects1[i].set_clipping_box(None)
        rects2[i].set_clipping_box(None)

# Set the linestyle of the same bars to 'dashed'
for i in range(len(professions)):
    if i == 3:
        rects1[i].set_linestyle('dashed')
        rects2[i].set_linestyle('dashed')
    else:
        rects1[i].set_linestyle(None)
        rects2[i].set_linestyle(None)

plt.tight_layout()
plt.savefig("myplot.png")