from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
social_media = ("Facebook", "Snapchat", "Instagram", "Twitter", "LinkedIn")
impact_on_teenagers = (85, 75, 90, 65, 45)

y = np.arange(len(social_media))  # the label locations
height = 0.25  # the height of the bars

fig, ax = plt.subplots()

# Creating the bar chart
bars = ax.barh(y, impact_on_teenagers, height, color='skyblue', edgecolor='blue')

# Adding labels to the bars
ax.bar_label(bars, padding=3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Impact Level')
ax.set_title('Impact of Social Media on Teenagers')
ax.set_yticks(y)
ax.set_yticklabels(social_media)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlim(0, 100)

# Adding grid and changing the face color
ax.grid(True)
ax.set_facecolor('lightgray')

# Saving the plot
plt.tight_layout()
plt.savefig("myplot.png")