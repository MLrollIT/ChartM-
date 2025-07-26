import matplotlib.pyplot as plt

# Age Groups
age_groups = ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]

# Internet Data Usage in GB
data_18_24 = [10, 15, 20, 25, 30]
data_25_34 = [20, 25, 30, 35, 40]
data_35_44 = [30, 35, 40, 45, 50]
data_45_54 = [40, 45, 50, 55, 60]
data_55_64 = [50, 55, 60, 65, 70]
data_65_plus = [10, 15, 20, 25, 30]

# Stack Plot
fig, ax = plt.subplots()

ax.stackplot(range(1, 6), data_18_24, data_25_34, data_35_44, data_45_54, data_55_64, data_65_plus, labels=age_groups)
ax.legend(loc="upper left")
ax.set_title('Internet Data Usage by Age Group', fontsize=16, fontweight='bold')
ax.set_xlabel('Time Duration', fontsize=14)
ax.set_ylabel('Internet Data Usage (in GB)', fontsize=14)
ax.grid(True)

# Set the clip box for the areas that contain the center point of the bounding box
bbox = plt.Bbox([[491, 127], [491 + 214, 127 + 341]])
ax.set_clip_box(bbox)

# Enable the picker state for these areas
ax.set_picker(True)

plt.tight_layout()
plt.savefig("figure.png")