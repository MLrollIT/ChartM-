import matplotlib.pyplot as plt

# Months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Pollution levels for all Cities
city_A = [42, 35, 48, 51, 55, 62, 68, 70, 63, 58, 47, 40]
city_B = [38, 31, 44, 48, 52, 60, 66, 68, 60, 55, 45, 36]
city_C = [46, 39, 52, 56, 60, 68, 74, 76, 70, 64, 53, 44]
city_D = [40, 33, 46, 49, 53, 61, 66, 68, 62, 56, 45, 38]

# Create a stack plot 
plt.figure(figsize=(10,7)) 
plt.stackplot(months, city_A, city_B, city_C, city_D, labels=['City A','City B','City C','City D'])
plt.legend(loc='upper left')
plt.title('City Pollution Levels Over a Year')
plt.xlabel('Months')
plt.ylabel('Pollution Index')

# Hide the filled area of the areas that contain the center point of the bounding box
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
center = bbox.center
bbox = plt.Rectangle((center[0] - 0.05, center[1] - 0.05), 0.1, 0.1, fill=False, edgecolor='none')
plt.gca().add_patch(bbox)

plt.tight_layout()
plt.savefig("figure.png")