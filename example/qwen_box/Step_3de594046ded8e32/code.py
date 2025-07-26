import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ozone_concentration = [265, 280, 290, 305, 320, 340, 355, 370, 360, 330, 290, 270]

# Create stair plot
plt.step(months, ozone_concentration, where='mid', label='Ozone concentration')

# Annotations
plt.title('Variations in Atmospheric Ozone Concentration Across Different Months')
plt.xlabel('Months')
plt.ylabel('Ozone Concentration (DU)')
plt.grid(True)

# Change marker face color and style of the lines that contain the center point of the bounding box
plt.plot(months, ozone_concentration, marker='o', markersize=10, color='#362753')

# Display plot
plt.legend()
plt.tight_layout()
plt.savefig("Edit_figure.png")