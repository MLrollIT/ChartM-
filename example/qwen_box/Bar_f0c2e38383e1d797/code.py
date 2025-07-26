from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
ai_technologies = ("Neural Networks", "Deep Learning", "Machine Learning", "Natural Language Processing", "Robotics", "Computer Vision", "Reinforcement Learning", "Predictive Analytics")
adoption_rates = (85, 70, 100, 60, 45, 90, 110, 65)

# Bar Plot
fig, ax = plt.subplots(facecolor='lightgrey')
y_pos = np.arange(len(ai_technologies)) 
bars = ax.barh(y_pos, adoption_rates, color='blue', edgecolor='black')

# Adding Labels
ax.set_xlabel('Adoption Rate (%)')
ax.set_ylabel('AI Technology')
ax.set_title('Adoption Rate of Various AI Technologies')
ax.set_yticks(y_pos)
ax.set_yticklabels(ai_technologies)
ax.invert_yaxis()  # labels read top-to-bottom
ax.grid(True)
ax.bar_label(bars, padding=3)

# Change clipping and snap state of bars containing the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5, 0.3, 0.3))
bars_to_modify = [bars[0], bars[1], bars[2]]
for bar in bars_to_modify:
    bar.set_clip_on(False)
    bar.set_snap(False)

plt.tight_layout()
plt.savefig("myplot.png")