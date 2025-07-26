from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# The given CSV data
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'China', 'Japan', 'Australia', 'Brazil'],
    '2018': [100, 120, 80, 120, 100, 90, 110, 90],
    '2019': [120, 180, 85, 125, 200, 150, 220, 180],
    '2020': [80, 150, 105, 90, 300, 90, 110, 90]
}

# The label locations, the height of the bars, and the multiplier
y = np.arange(len(data['Country']))
height = 0.25
multiplier = 0

# Creating the bar chart
fig, ax = plt.subplots()

for year in ['2018', '2019', '2020']:
    offset = height * multiplier
    bars = ax.barh(y + offset, data[year], height, label=year, color=['red', 'blue', 'green'][multiplier], edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Adding labels, title, tick labels, and legend
ax.set_xlabel('Score')
ax.set_title('Score by Country and Year')
ax.set_yticks(y + height)
ax.set_yticklabels(data['Country'])
ax.legend(loc='upper right', ncol=1)

# Inverting y-axis and setting x-axis limit
ax.invert_yaxis()
ax.set_xlim(0, 350)

# Adding grid and changing background color
ax.grid(True)
ax.set_facecolor('gray')

plt.tight_layout()
plt.savefig("myplot.png")