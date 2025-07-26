from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set the data
types_of_vehicles = ["Hybrid Electric Vehicles", 
                     "Plug-in Hybrid Electric Vehicles", 
                     "Battery Electric Vehicles", 
                     "Fuel Cell Electric Vehicles"]
percentages = [25, 30, 40, 5]

# Draw the pie chart
wedges, texts, autotexts = ax.pie(percentages, 
                                   explode=(0.1, 0, 0, 0), 
                                   labels=types_of_vehicles, 
                                   autopct='%1.1f%%',
                                   pctdistance=0.85,
                                   shadow=True,
                                   startangle=140)

# Draw white circle in the middle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Set the title
ax.set_title("Percentage of Different Electric Vehicle Types")

# Set the background color
ax.set_facecolor('gray')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")