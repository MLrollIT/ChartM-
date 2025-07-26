import matplotlib.pyplot as plt

# Depth levels
depth_levels = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Volumes of different architectural elements
temple_ruins_vol = [100, 250, 300, 200, 150, 100, 50, 25, 10, 5]
palace_halls_vol = [150, 200, 180, 130, 100, 80, 60, 40, 20, 10]
coral_garden_vol = [50, 80, 100, 110, 120, 100, 80, 60, 40, 20]

# Plot the stack plot
plt.figure(figsize=(10,7))
plt.stackplot(depth_levels, temple_ruins_vol, palace_halls_vol, coral_garden_vol, 
              labels=['Ancient Temple Ruins', 'Sunken Palace Halls', 'Coral Garden Structures'], 
              colors=['sienna', 'coral', 'skyblue'], alpha=0.7)

# Set the labels and title
plt.xlabel('Depth Levels (meters)')
plt.ylabel('Volume of Structures (cubic meters)')
plt.title('Volumetric Analysis of Architectural Elements in a Mystical Underwater City')
plt.legend(loc='upper right')

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")