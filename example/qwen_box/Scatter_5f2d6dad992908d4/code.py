from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

data = {"Type_of_Travel":["Car Travel","Train Travel","Flight Travel","Bus Travel"],
        "Popularity":[70,90,50,30]}

fig, ax = plt.subplots()

# Updated to set scatter points to blue
ax.scatter(data["Type_of_Travel"], data["Popularity"], marker='o', color='blue')
for i, txt in enumerate(data["Type_of_Travel"]):
    # Updated to set annotation text to red
    ax.annotate(txt, (data["Type_of_Travel"][i], data["Popularity"][i]), color='red')
    
ax.set_xlabel('Type of Travel', fontsize=15)
ax.set_ylabel('Popularity', fontsize=15)
ax.set_title('Popularity of Different Types of Travel')
ax.grid(True)
ax.set_facecolor('gray')

fig.tight_layout()
plt.savefig("myplot.png")