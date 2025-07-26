from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Define the data
allergy_type = ["Dust Mites", "Pollens", "Dairy"]
prevalence = [[15,17,13,16,20,18,15,20,17,25,12,15,13,18,17,20,16,19,17,16],
              [25,28,24,23,22,30,34,33,32,30,40,35,39,36,38,32,30,28,27,25],
              [20,22,25,20,18,17,16,15,17,30,18,18,20,19,14,15,16,20,18,20]]

# Create the scatter chart
fig, ax = plt.subplots()

for i, type in enumerate(allergy_type):
    ax.scatter(np.arange(len(prevalence[i])), prevalence[i], label=type)

# Add labels, title, legend, and grid
ax.set_xlabel('Time')
ax.set_ylabel('Prevalence')
ax.set_title('Prevalence of Different Allergies Over Time')
ax.legend()
ax.grid(True)

# Annotate each point
for i, type in enumerate(allergy_type):
    for j, p in enumerate(prevalence[i]):
        ax.text(j, p, str(p))

# Change the background color to white
ax.set_facecolor('white')  # Modified line

# Tight layout and save figure
plt.tight_layout()
plt.savefig("myplot.png")