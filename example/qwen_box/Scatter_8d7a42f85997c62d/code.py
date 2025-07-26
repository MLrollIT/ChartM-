import matplotlib.pyplot as plt

# Temperatures 
temp_A = [30, 32, 34, 33, 30, 31]
temp_B = [29, 31, 30, 32, 33, 31]
temp_C = [28, 29, 30, 29, 28, 30]
temp_D = [31, 33, 32, 34, 33, 30]
temp_E = [32, 34, 33, 35, 34, 32]

# Rainfalls
rain_A = [150, 200, 120, 180, 100, 140]
rain_B = [100, 120, 150, 130, 140, 110]
rain_C = [80, 100, 90, 70, 80, 100]
rain_D = [200, 220, 180, 240, 200, 180]
rain_E = [250, 280, 230, 270, 250, 260]

plt.figure(figsize=(10, 6))

# Scatter plots
plt.scatter(temp_A, rain_A, label = 'Region A', s=36, color='#66b815')
plt.scatter(temp_B, rain_B, label = 'Region B')
plt.scatter(temp_C, rain_C, label = 'Region C')
plt.scatter(temp_D, rain_D, label = 'Region D')
plt.scatter(temp_E, rain_E, label = 'Region E')

# Titles and labels
plt.title('Rainfall vs Temperature in Tropical Regions')
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')

# Legend
plt.legend()

plt.tight_layout()
plt.savefig("figure.png")