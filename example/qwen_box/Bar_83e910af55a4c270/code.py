from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data
data = '''Age_Group,Hours_Weekdays,Hours_Weekends,Hours_Holidays
Under_20,30,15,45
20_to_30,35,20,60
30_to_40,40,25,55
Above_40,20,10,30'''

# Create a pandas DataFrame from the csv data
df = pd.read_csv(StringIO(data))

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars_weekdays = ax.bar(df['Age_Group'], df['Hours_Weekdays'], color='skyblue', edgecolor='black')
bars_weekends = ax.bar(df['Age_Group'], df['Hours_Weekends'], color='green', edgecolor='black', bottom=df['Hours_Weekdays'])
bars_holidays = ax.bar(df['Age_Group'], df['Hours_Holidays'], color='red', edgecolor='black', bottom=df['Hours_Weekdays'] + df['Hours_Weekends'])

# Set title, x-label and y-label
ax.set_title('Hours spent by Age Group')
ax.set_xlabel('Age Group')
ax.set_ylabel('Hours')

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend
ax.legend(["Weekdays", "Weekends", "Holidays"], loc='upper right')

# Add the corresponding value at the end of each bar
ax.bar_label(bars_weekdays, label_type='center')
ax.bar_label(bars_weekends, label_type='center')
ax.bar_label(bars_holidays, label_type='center')

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")