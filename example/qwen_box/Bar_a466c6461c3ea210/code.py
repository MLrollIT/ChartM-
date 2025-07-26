from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# The csv data
csv_data = "Age_Group,Online_Shop_Habits\n18-24,320\n25-34,520\n35-44,430\n45-54,700\n55-64,750\n65-74,800\n75-84,1000\n85+,1100\n<unknown>,500"
df = pd.read_csv(StringIO(csv_data))

# Set the figure size and create bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df['Age_Group'], df['Online_Shop_Habits'], color='skyblue', edgecolor='black')

# Set the title, x-label, and y-label
ax.set_title('Online Shopping Habits by Age Group')
ax.set_xlabel('Age Group')
ax.set_ylabel('Online Shop Habits')

# Add the data value on top of each bar
ax.bar_label(bars, label_type='center')

# Remove grid and set the background color to white
ax.grid(False) # This line removes the grid
ax.set_facecolor('white') # This line changes the background color to white

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")