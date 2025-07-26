from io import StringIO
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

# Given data
data = {
    "": ["Homecooked Meals", "Restaurant Meals", "Online Food Delivery", "Meal Kits", "Instant Meals", "Traditional Recipes", "Experimental Cooking", "Healthy Meals"],
    "Prep Time": [100, 65, 40, 85, 60, 120, 80, 95],
    "Cooking Time": [75, 90, 55, 70, 85, 100, 60, 80],
    "Serving Size": [80, 55, 60, 68, 75, 95, 70, 85]
}
df = pd.DataFrame(data)

# Plotting the data
fig, ax = plt.subplots()

# Variables for line styles and colors
line_styles = ['-', '--', '-.', ':']
colors = ['red', 'green', 'blue', 'purple', 'cyan', 'magenta', 'yellow', 'orange']

# Plotting each column with different style
for i, column in enumerate(df.columns[1:]):
    ax.plot(df[column], linestyle=line_styles[i % len(line_styles)], color=colors[i % len(colors)], 
            linewidth=2, marker='o', markersize=5, alpha=0.463, label=column)

# Adding title and labels
ax.set_title('Preparation and Serving Time for Different Meals')
ax.set_xlabel('Meal Types')
ax.set_ylabel('Time (minutes)')

# Setting xticks
ax.set_xticks(np.arange(len(df[""])))
ax.set_xticklabels(df[""])

# Setting the background color
ax.set_facecolor('lightgray')

# Adding grid
ax.grid(True)

# Adding legend
ax.legend()

# Annotating each line
for i, txt in enumerate(df['Prep Time']):
    ax.annotate('Prep Time', (i, txt), textcoords="offset points", xytext=(10,10), ha='center')
for i, txt in enumerate(df['Cooking Time']):
    ax.annotate('Cooking Time', (i, txt), textcoords="offset points", xytext=(10,10), ha='center')
for i, txt in enumerate(df['Serving Size']):
    ax.annotate('Serving Size', (i, txt), textcoords="offset points", xytext=(10,10), ha='center')

plt.tight_layout()
plt.savefig('myplot.png')