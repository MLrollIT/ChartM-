from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

disorders = ["Anxiety Disorders", "Mood Disorders", "Schizophrenia", "Mood Disorders", "Schizophrenia", "Anxiety Disorders"]
prevalence = [12, 15, 8, 10, 6, 18]
data = np.array([12, 15, 8, 10, 6, 18])

fig, ax = plt.subplots()
im = ax.imshow(data.reshape(3,2), cmap='plasma', alpha=0.8)  # Changed colormap to 'plasma'

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(2), labels=["First", "Second"])
ax.set_yticks(np.arange(3), labels=list(set(disorders)))

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(set(disorders))):
    for j in range(2):
        text = ax.text(j, i, data[i*2+j],
                       ha="center", va="center", color="black")  # Changed text color to black

ax.set_title("Prevalence of Mental Health Disorders")
ax.set_xlabel("Measurement")
ax.set_ylabel("Mental Health Disorder")
ax.grid(True)
ax.set_facecolor('lightgray')

fig.tight_layout()
plt.savefig("myplot.png")