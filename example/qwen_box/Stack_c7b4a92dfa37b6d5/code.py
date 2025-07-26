import matplotlib.pyplot as plt

# Ocean depths
depths = ['0-200m', '200-500m', '500-1000m', '1000-2000m', 'Below 2000m']

# Oceanic currents at different depths
current1 = [0.8, 0.5, 0.2, 0.4, 0.1]
current2 = [0.7, 0.4, 0.3, 0.2, 0.2]
current3 = [0.6, 0.3, 0.1, 0.3, 0.1]

# Creating stack plot
plt.figure(figsize=(10,6))
plt.stackplot(depths, current1, current2, current3, labels=['Current 1','Current 2','Current 3'])

plt.legend(loc='upper right')
plt.title('Oceanic Currents at Different Depths')
plt.xlabel('Ocean Depths')
plt.ylabel('Oceanic Current Speed (m/s)')


plt.tight_layout()
plt.savefig("figure.png")