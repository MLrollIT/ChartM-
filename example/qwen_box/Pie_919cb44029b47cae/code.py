from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Prepare the data with updated values
data = {
    "Year": ["2010","2011","2012","2013","2014","2015","2016","2017","2018"],
    "Percentage": [9, 10, 13, 14, 15, 17, 18, 10, 9]  # Updated data values
}

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'purple', 'pink', 'yellow', 'orange']
explode = np.zeros_like(data["Percentage"])  # explode 1st slice
explode[0] = 0.1  

# Plot with updated data
ax.pie(data["Percentage"], explode=explode, labels=data["Year"], colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax.set_title("Yearly Percentage Change")
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig.set_facecolor('grey')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")