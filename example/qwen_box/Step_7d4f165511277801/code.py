# Import the required library
import matplotlib.pyplot as plt

# Data for x-axis (Depth Levels in meters)
depth_levels = [0, 10, 20, 30, 40, 50]

# Data for y-axis (Temperature and Salinity levels)
temperature = [24, 23.5, 22.8, 20.5, 18.9, 17]
salinity = [35, 35.2, 35.4, 35.6, 35.8, 36]

# Create a new figure and a subplot
fig, ax_temp = plt.subplots()

# Temperature plot 
ax_temp.step(depth_levels, temperature, where='mid', color='tab:red')
ax_temp.set_xlabel('Depth Levels in meters')
ax_temp.set_ylabel('Temperature in °C', color='tab:red')
ax_temp.tick_params(axis='y', labelcolor='tab:red')

# Instantiate a second axes that shares the same x-axis
ax_salinity = ax_temp.twinx()
ax_salinity.step(depth_levels, salinity, where='mid', color='tab:blue')
ax_salinity.set_ylabel('Salinity Levels in ppt', color='tab:blue') 
ax_salinity.tick_params(axis='y', labelcolor='tab:blue')

# Add grid and title
plt.grid()
plt.title('Depth Vs Temperature and Salinity Levels')

# Display plot

plt.tight_layout()
plt.savefig("figure.png")