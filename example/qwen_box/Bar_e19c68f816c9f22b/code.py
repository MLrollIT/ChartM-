from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = StringIO("""
Age_Group,TV_Hours_2010,TV_Hours_2020
Under_18,1.2,0.8
18-24,2.5,1.3
25-34,3.0,2.8
35-44,3.5,2.9
45-54,4.0,3.8
55-64,4.5,3.5
65_and_above,5.0,4.5
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

# Plotting the data with new colors
bars1 = ax.bar(df['Age_Group'], df['TV_Hours_2010'], color='purple', edgecolor='black', width=0.4, label='TV_Hours_2010')
bars2 = ax.bar(df['Age_Group'], df['TV_Hours_2020'], color='orange', edgecolor='black', width=0.4, label='TV_Hours_2020', bottom=df['TV_Hours_2010'])

# Adding labels
ax.set_title("TV Watching Hours in 2010 and 2020 by Age Group")
ax.set_xlabel("Age Group")
ax.set_ylabel("TV Watching Hours")
ax.legend(loc="upper right")

# Adding data labels
ax.bar_label(bars1, label_type='center')
ax.bar_label(bars2, label_type='center')

# Adding grid
ax.grid(True)

# Changing the face color to white
ax.set_facecolor('white')

# Save chart as a png file
plt.tight_layout()
plt.savefig("myplot.png")