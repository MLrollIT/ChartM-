from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Data
labels = 'Malware', 'Phishing', 'Password Attacks', 'Denial of Service', 'Man in the Middle', 'Advanced Persistent Threats'
sizes = [30, 25, 15, 10, 10, 10]  # Convert the percentages to integers

# Plot
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%', explode=(0.1, 0, 0, 0, 0, 0), labeldistance=1.05, shadow=True, pctdistance=0.85, colors=['red', 'green', 'blue', 'yellow', 'purple', 'orange'])

# Set title, legend, and face color
plt.title("Distribution of Cybersecurity Threats") 
plt.legend(labels, title="Threats", loc="upper right") 
fig.set_facecolor('lightgray')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")