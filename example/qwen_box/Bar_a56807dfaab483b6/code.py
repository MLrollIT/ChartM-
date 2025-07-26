from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {
    'Year': [1990, 2000, 2010, 2020],
    'Liberalism': [200, 210, 220, 250],
    'Conservatism': [250, 230, 220, 300],
    'Socialism': [300, 280, 260, 240],
    'Libertarianism': [350, 370, 400, 360]
}

# Prepare x-axis labels
years = data.pop('Year')

# Prepare y-values and labels
values = list(data.values())
labels = list(data.keys())

# Create figure and axis
fig, ax = plt.subplots()

# Set the bar width and position
width = 0.2
x = np.arange(len(years))

# Plot bars
for i in range(len(labels)):
    bars = ax.bar(x - width/2 + i*width, values[i], width, label=labels[i])
    ax.bar_label(bars, label_type='center')

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Supporters')
ax.set_title('Political Ideology Supporters over Years')

# Set x-ticks
ax.set_xticks(x)
ax.set_xticklabels(years)

# Set legend
ax.legend(loc='upper right', ncol=1)

# Add grid and set background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Save the plot
plt.tight_layout()
plt.savefig("myplot.png")