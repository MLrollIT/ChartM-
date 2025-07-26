import matplotlib.pyplot as plt

# Data
density_ranges = ['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
dust_particles = [15, 22, 18, 25, 12, 16, 9]

# Create Figure and Axis
fig, ax = plt.subplots()

# Create Histogram
ax.bar(density_ranges, dust_particles, color='skyblue', edgecolor='black')

# Set Labels and Title
ax.set_xlabel('Density Range of Cosmic Dust', fontsize=14)
ax.set_ylabel('Amount of Dust Particles', fontsize=14)
ax.set_title('Cosmic Dust Distribution in Galaxy', fontsize=16)

# Modify the object in the chart
for bar in ax.patches:
    if bar.get_label() == 'A new Label':
        bar.set_facecolor('#f5976c')

# Show Figure
plt.tight_layout()
plt.savefig("figure.png")