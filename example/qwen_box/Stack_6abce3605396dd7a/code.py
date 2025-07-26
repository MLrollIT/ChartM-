import matplotlib.pyplot as plt

# Data
years = [2016, 2017, 2018, 2019, 2020]
evs = [30, 28, 26, 24, 22]
gps = [3, 3.5, 3.2, 2.8, 2.5]

plt.figure(figsize=(10,7))

# Creating the stack plot
plt.stackplot(years, evs, gps, labels=['EVs (KWh/100 Miles)', 'GPs (Gallons/100 Miles)'])

# Adding additional details  
plt.title('Comparison of Energy Consumption between EVs and GPs (2016-2020)')
plt.xlabel('Years')
plt.ylabel('Energy Consumption')
plt.legend(loc='upper left')

# Change the alpha blending mode of the area that includes the center point of the bounding box to 0.4375
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.5
bbox[1] = 0.5
bbox[2] = 0.5
bbox[3] = 0.5
plt.gca().set_position(bbox)
plt.gca().patch.set_alpha(0.4375)

plt.tight_layout()
plt.savefig("figure.png")