import matplotlib.pyplot as plt

# Data
crystal_sizes = ["Small", "Medium", "Large"]
growth_rates_T1 = [3, 2, 1]
growth_rates_T2 = [4, 3, 2]
growth_rates_T3 = [5, 4, 3]

# Create a stack plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(crystal_sizes, growth_rates_T1, growth_rates_T2, growth_rates_T3, labels=['T1','T2','T3'])

# Labels and Titles
ax.set_xlabel("Crystal Sizes")
ax.set_ylabel("Growth Rates")
ax.set_title("Crystal Formation Kinetics in 3D")
ax.legend(loc="upper left")

# Change the face color of the area that contains the center point of the bounding box to #97e001
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox = ax.bbox_to_anchor((0.35, 0.35), pad=10)
bbox