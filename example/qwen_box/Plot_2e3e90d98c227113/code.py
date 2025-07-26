from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Allergies': ['Peanuts', 'Dairy', 'Gluten', 'Shellfish', 'Pollen', 'Mold', 'Dust Mites'],
    'Year1': [100, 50, 80, 70, 100, 90, 70],
    'Year2': [80, 45, 75, 65, 50, 95, 60],
    'Year3': [75, 50, 70, 40, 60, 110, 80],
    'Year4': [150, 45, 72, 41, 110, 80, 70]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()
for index, row in df.iterrows():
    ax.plot(['Year1', 'Year2', 'Year3', 'Year4'], row[1:], label=row[0], marker='o')
    for x, y in zip(['Year1', 'Year2', 'Year3', 'Year4'], row[1:]):
        ax.text(x, y, f'{y}', ha='right')

ax.set_title('Allergies Over Years')
ax.set_xlabel('Years')
ax.set_ylabel('Allergies')
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')

plt.tight_layout()
plt.savefig("myplot.png")