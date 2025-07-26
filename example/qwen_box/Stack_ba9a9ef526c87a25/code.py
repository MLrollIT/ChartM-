import matplotlib.pyplot as plt

# defining the checkpoints
checkpoints = ["Checkpoint 1", "Checkpoint 2", "Checkpoint 3", "Checkpoint 4", "Checkpoint 5"]

# defining the elevation data
elevation = [50, 75, 45, 60, 80]

# defining the water flow data
water_flow = [10, 15, 8, 12, 18]

# plotting the elevation and water flow stackplot
fig, ax = plt.subplots(figsize=(10, 7))

ax.stackplot(checkpoints, elevation, water_flow, labels=['Elevation (m)','Water Flow (m³/s)'], colors=['#6d904f', '#fc4f30'], alpha=0.7 )

# adding the additional details like legend, title and labels
ax.legend(loc='upper left')
ax.set_title('Elevation and Water Flow along a River', fontsize=18)
ax.set_xlabel('Checkpoints', fontsize=12)
ax.set_ylabel('Height (m) / Water Flow (m³/s)',fontsize=12)

# adding the bounding box and label
bbox = dict(boxstyle="square", fc="#323ad4", ec="black", lw=2)
ax.text(0.5, 0.5, 'A new Label', transform=ax.transAxes, fontsize=14, verticalalignment='center', horizontalalignment='center', bbox=bbox)

# displaying the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")