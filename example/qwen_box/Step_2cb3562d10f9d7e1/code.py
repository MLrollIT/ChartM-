from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040])
moon_missions = np.array([12, 22, 16, 14, 8, 5, 2, 6, 10])
mars_missions = np.array([5, 7, 12, 10, 14, 11, 20, 25, 30])

# Plotting the data
plt.step(decades, moon_missions, label='Moon Missions', color='blue', linewidth=2, marker='o', markersize=8, alpha=0.7, linestyle='-')
plt.step(decades, mars_missions, label='Mars Missions', color='red', linewidth=2, marker='v', markersize=8, alpha=0.7, linestyle='--')

# Annotating the lines
for i, txt in enumerate(moon_missions):
    plt.annotate('Moon Missions', (decades[i], moon_missions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue')
for i, txt in enumerate(mars_missions):
    plt.annotate('Mars Missions', (decades[i], mars_missions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

# Setting the chart title and labels
plt.title('Moon vs Mars Missions per Decade')
plt.xlabel('Decade')
plt.ylabel('Number of Missions')

# Adding a grid
plt.grid(True)

# Setting the background color
plt.gca().set_facecolor('gray')

# Adding a legend
plt.legend()

# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig("myplot.png")