import matplotlib.pyplot as plt

# Depth ranges
depth_ranges = ['1000-2000m', '2000-3000m', '3000-4000m', '4000-5000m']

# Abundance of species at different depth
giant_squid = [15, 20, 18, 22]
anglerfish = [10, 12, 15, 18]
vampire_squid = [5, 8, 6, 7]

# Graph plotting
plt.figure(figsize=(10, 6))

plt.stackplot(depth_ranges, giant_squid, anglerfish, vampire_squid, labels=['Giant Squid', 'Anglerfish', 'Vampire Squid'])

plt.legend(loc='upper left')

plt.title('Deep Sea Creature Distribution Mapping')
plt.xlabel('Depth Range')
plt.ylabel('Total Counts')

plt.tight_layout()
plt.savefig("figure.png")