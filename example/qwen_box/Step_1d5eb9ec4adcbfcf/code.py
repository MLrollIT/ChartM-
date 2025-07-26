import matplotlib.pyplot as plt

# Data points for the number of unique species at different depths in each region
regions = ['Region A', 'Region B', 'Region C']
depths = [100, 200, 300, 400, 500]
species_counts = {
    'Region A': [12, 19, 24, 21, 16],
    'Region B': [10, 13, 15, 12, 9],
    'Region C': [15, 22, 26, 20, 18]
}

fig, ax = plt.subplots(figsize=(10, 6))

for region in regions:
    ax.step(depths, species_counts[region], label=region)

ax.set(xlabel='Depth (m)', ylabel='Number of Unique Species',
       title='Alien Ecosystem Diversity in 3D')
ax.grid()
plt.legend()


plt.tight_layout()
plt.savefig("figure.png")