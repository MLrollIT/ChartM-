from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import pandas as pd

data = StringIO("""
Profession,Rate
Doctors,40
Lawyers,45
Teachers,60
Engineers,35
Nurses,70
""")

df = pd.read_csv(data)
professions = df['Profession'].values
rates = df['Rate'].values

y = np.arange(len(professions))  # the label locations

fig, ax = plt.subplots()

bars = ax.barh(y, rates, color='skyblue', edgecolor='blue')

# Add bar labels
ax.bar_label(bars, padding=3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Rate')
ax.set_ylabel('Profession')
ax.set_title('Rate of different professions')
ax.set_yticks(y)
ax.set_yticklabels(professions)
ax.grid(visible=True)
ax.set_facecolor('lightgray')

# Invert the y-axis so the professions read top-to-bottom
ax.invert_yaxis()

# Set the transparency of the bars that contain the center point of the bounding box to 0.94
for bar in bars:
    if bar.contains((35, 35)):
        bar.set_alpha(0.94)
        bar.set_picker(True)

plt.tight_layout()
plt.savefig("myplot.png")