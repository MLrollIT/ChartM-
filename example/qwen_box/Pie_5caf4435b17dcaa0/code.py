from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Data
labels = ["South Asia", "Sub-Saharan Africa", "Latin America & Caribbean", "East Asia & Pacific"]
sizes = [35, 25, 20, 20]

fig, ax = plt.subplots()

# Plotting
ax.pie(sizes, labels=labels, autopct='%1.1f%%', labeldistance=1.05, shadow=True, pctdistance=0.8, colors=['red', 'green', 'blue', 'yellow'])
fig.set_facecolor("lightgrey")

# Adding title, legend
plt.title("Child Mortality Rate Reduction by Region") 
plt.legend(labels, title="Regions", loc="upper right") 

plt.tight_layout()
plt.savefig("myplot.png")