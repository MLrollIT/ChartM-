from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# CSV data
data = {
    "Demographics": ["Youths (12-18)", "Adults (19-60)", "Seniors (61+)"],
    "Percentage": [30, 50, 20]
}

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
ax.set_facecolor('gray')

# Draw pie chart
wedges, texts, autotexts = ax.pie(data["Percentage"], explode=(0.1, 0, 0), labels=data["Demographics"], autopct='%1.1f%%', shadow=True, startangle=90)

# Draw white circles at the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Title
plt.title('Demographic Distribution')

# Legends
plt.legend(wedges, data["Demographics"],
          title="Demographics",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig("myplot.png")