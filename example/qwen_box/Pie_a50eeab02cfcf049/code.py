from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Provided data
data = {"Factors": ["Accessibility", "Cost Efficiency", "Flexibility", "Student Engagement", "Self-paced Learning", "Improved Technical Skills", "Others"],
        "Percentage": [15, 20, 25, 10, 15, 10, 5]}

labels = data["Factors"]
sizes = data["Percentage"]

fig, ax = plt.subplots()

# New custom palette
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f']

# Additional parameters
explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Accessibility')

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)

# Setting title, labels, and legend
plt.title("Factors Influencing Online Learning") # Add title
plt.legend(labels, title="Factors", loc="upper right") # Add legend

# Setting face color to white
fig.patch.set_facecolor('white')

plt.tight_layout()
plt.savefig("myplot.png")