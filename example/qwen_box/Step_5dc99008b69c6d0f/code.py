from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given data
data = {
    "Type of Alcohol": ["Beer", "Wine", "Spirits", "Beer", "Wine", "Spirits", "Beer"],
    "Consumption": [100, 120, 80, 70, 150, 50, 90]
}

df = pd.DataFrame(data)

# Sorting and grouping data by type of alcohol and getting the mean consumption
grouped_df = df.groupby('Type of Alcohol').mean()

x = np.array(grouped_df.index)
y = np.array(grouped_df["Consumption"])

plt.figure(facecolor='gray')

# Plotting the data
plt.step(x, y, linestyle=':', linewidth=2, color='green', marker='o', markersize=5, alpha=0.7, label="Consumption")

plt.grid(axis='both', color='0.95')

# Adding labels and title
plt.xlabel('Type of Alcohol')
plt.ylabel('Consumption')
plt.title('Alcohol Consumption')

# Adding legend
plt.legend()

for i, txt in enumerate(y):
    plt.annotate(txt, (x[i], y[i]), fontsize=12, color='#925fa5')

plt.tight_layout()
plt.savefig("myplot.png")