import matplotlib.pyplot as plt

# Year Data
years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]

# Adoption Rates Data
gen_x = [20, 30, 40, 55, 70, 80, 85]
millennials = [5, 15, 30, 50, 65, 80, 95]
gen_z = [0, 1, 10, 30, 55, 70, 85]
baby_boomers = [50, 35, 20, 10, 5, 2, 1]

# Plotting the Data
plt.figure(figsize=(10,6))
plt.scatter(years, gen_x, color='r', label='Generation X')
plt.scatter(years, millennials, color='g', label='Millennials')
plt.scatter(years, gen_z, color='b', label='Generation Z')
plt.scatter(years, baby_boomers, color='y', label='Baby Boomers')

# Adding Labels and Title
plt.xlabel('Years')
plt.ylabel('Adoption Rate (%)')
plt.title('Technology Adoption Rates Among Different Generations')

# Adding a Legend
plt.legend()

# Set the size of the scatter points that share the same legend as those containing the center point of the bounding box to 99.
# Apply a shadow effect to these points with an offset of 7.7 pixels and a gold foreground color.
plt.scatter(years[4], gen_x[4], color='r', s=99, label='Generation X', alpha=0.5, edgecolors='none', facecolors='none', shadow=True, offset=[7.7, 0], c='gold')

# Display the Plot

plt.tight_layout()
plt.savefig("figure.png")