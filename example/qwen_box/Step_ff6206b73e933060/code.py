import matplotlib.pyplot as plt

# Initialize time intervals (in nanoseconds) and corresponding energy levels (in kJ/mol)
time_intervals = [0, 1, 2, 3, 4, 5] # in nanoseconds
energy_levels = [100, 95, 85, 75, 80, 90] # in kJ/mol

plt.figure(figsize=(10, 6))

# Creating the stair plot
plt.step(time_intervals, energy_levels, where='post')

# Set labels and title
plt.xlabel('Time Intervals (ns)')
plt.ylabel('Energy Levels (kJ/mol)')
plt.title('Molecular Dynamics Simulations of Protein Folding Dynamics')

# Set the x and y axis limits
plt.xlim([0, 5])
plt.ylim([70, 110])

# Showing the plot
plt.grid(True)

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform((3, 75))

# Set the visibility of the lines that contain the center point of the bounding box to False
for line in plt.gca().lines:
    if bbox.contains(line.get_xydata()[0]):
        line.set_visible(False)

plt.tight_layout()
plt.savefig("Edit_figure.png")