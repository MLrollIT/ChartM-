import matplotlib.pyplot as plt
import numpy as np

ind = np.arange(5)  # the x locations for the groups
width = 0.35  # the width of the bars

# Data for Fuel Combustion
fc = np.array([[15, 18, 20, 22, 19], [8, 10, 12, 15, 11], [5, 6, 7, 8, 6]])

# Data for Exhaust Gases
eg = np.array([[12, 14, 16, 18, 15], [7, 9, 10, 13, 10], [4, 5, 6, 7, 5]])

# Data for Cooling Systems
cs = np.array([[10, 12, 14, 16, 13], [5, 7, 8, 10, 7], [3, 4, 5, 6, 4]])

# Create a sub-plot for Fuel Combustion
plt.figure(figsize=(10, 6))
plt.stackplot(ind, fc, labels=['Component 1','Component 2','Component 3'], alpha=0.5)
plt.title('Fluid Dynamics in Rocket Engines : Fuel Combustion')
plt.legend()

# Create a sub-plot for Exhaust Gases
plt.figure(figsize=(10, 6))
plt.stackplot(ind, eg, labels=['Component 1','Component 2','Component 3'], alpha=0.5)
plt.title('Fluid Dynamics in Rocket Engines : Exhaust Gases')
plt.legend()

# Create a sub-plot for Cooling Systems
plt.figure(figsize=(10, 6))
plt.stackplot(ind, cs, labels=['Component 1','Component 2','Component 3'], alpha=0.5)
plt.title('Fluid Dynamics in Rocket Engines : Cooling Systems')
plt.legend()


plt.tight_layout()
plt.savefig("figure.png")