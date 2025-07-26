from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
age_group = ["Under 20", "20-40", "40 and above"]
consumption_percentage = [30, 45, 25]

# Additional parameters for the pie chart
explode = (0.1, 0, 0)  # Only "explode" the 1st slice (i.e. 'Under 20')
colors = ['blue', 'green', 'red']  # Changed the segment colors

# Create a new figure, with a single axis
fig1, ax1 = plt.subplots()

# Plot the pie chart
ax1.pie(consumption_percentage, explode=explode, labels=age_group, colors=colors, autopct='%1.1f%%', 
        shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  

# Set the title and labels
plt.title('Fast Food Consumption Percentage by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Consumption Percentage')

# Set the background color
ax1.set_facecolor('whitesmoke')  # Changed the background color

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")