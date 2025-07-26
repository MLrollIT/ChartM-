from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# CSV data
data_csv = [
    ["Electric Vehicle Components","Percentage"],
    ["Battery","40%"],
    ["Motor","30%"],
    ["Charging Infrastructure","20%"],
    ["Regenerative Braking System","5%"],
    ["Other Components","5%"]
]

# Extracting the components and their respective percentages
components = [row[0] for row in data_csv[1:]]
percentages = [float(row[1].strip('%')) for row in data_csv[1:]]

# Creating a pie chart
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(percentages, explode=(0.1, 0, 0, 0, 0), labels=components, autopct='%1.1f%%', shadow=True, startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])

# Adding a legend
ax.legend(wedges, components, title="Electric Vehicle Components", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adding title and labels
ax.set_title("Electric Vehicle Component Distribution")
plt.xlabel("Components")
plt.ylabel("Percentage")

# Setting background color to white
fig.patch.set_facecolor('white')

# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the animated state of the slice that contains the center point of the bounding box to False
for autotext in autotexts:
    autotext.set_visible(False)

# Update the label of the slice to 'A new Label'
for text in texts:
    text.set_text('A new Label')

# Save the modified figure
plt.savefig("Edit_figure.png")