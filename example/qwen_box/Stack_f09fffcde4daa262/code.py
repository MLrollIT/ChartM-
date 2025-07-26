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

# Set the clipping box for the areas that contain the center point of the bounding box
bbox = plt.Bbox([[121, 140], [121 + 338, 140 + 297]])
plt.clipbox(bbox, facecolor='#3be6b5')

plt.tight_layout()
plt.savefig("figure.png")