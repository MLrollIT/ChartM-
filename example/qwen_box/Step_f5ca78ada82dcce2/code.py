import matplotlib.pyplot as plt 

# Regions under observation
regions = ['Region A', 'Region B', 'Region C', 'Region D']

# Temperature recorded for each region before and after the initiatives
temp_before = [18, 22, 20, 25]
temp_after = [16, 20, 19, 23]

# Plotting
plt.figure(figsize=(10, 6))
plt.step(regions, temp_before, label='Before Initiatives', where='mid')
plt.step(regions, temp_after, label='After Initiatives', where='mid')

# Legends, title and labels
plt.legend(loc='best')
plt.title('Comparison of average temperatures before and after urban greening initiatives')
plt.xlabel('Regions')
plt.ylabel('Average Temperature (°C)')

# To start y-axis at 0
plt.ylim(bottom=0)

# Change the dash pattern of the step line that contains the center point of the bounding box to '-.'
plt.step(regions[1], temp_before[1], label='Before Initiatives', where='mid', dashes=[1, 1])

plt.tight_layout()
plt.savefig("Edit_figure.png")