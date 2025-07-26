import matplotlib.pyplot as plt

# Time intervals
time_intervals = ['6:00 AM', '12:00 PM', '6:00 PM', '12:00 AM']

# Temperature distribution in each ocean layer
temp_surface_layer = [20,22,24,20]
temp_thermocline_layer = [18,16,14,16]
temp_deep_ocean_layer = [10,8,6,9]
temp_abyssal_layer = [4,3,2,3]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Creating the stack plot
ax.stackplot(time_intervals, temp_surface_layer, temp_thermocline_layer, 
             temp_deep_ocean_layer, temp_abyssal_layer, 
             labels=['Surface (0m-100m)','Thermocline (100m-500m)','Deep Ocean (500m-1000m)','Abyssal (>=1000m)'],
             alpha=0.6)

# Customizing the plot
ax.set_title('Temperature Distribution in Ocean Layers Over 24-Hour Period')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Temperature (°C)')
ax.legend(loc='upper left')

# Show graph

plt.tight_layout()
plt.savefig("figure.png")