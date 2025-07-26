import matplotlib.pyplot as plt
import seaborn as sns

# avalanche sizes at different altitude bands
altitude_band_1 = [1500, 1800, 1750, 1400, 1650, 1850, 1700, 1600, 1550, 1450]
altitude_band_2 = [2200, 2500, 2350, 2400, 2300, 2100, 2700, 2250, 2650, 2450]
altitude_band_3 = [3200, 3100, 3400, 3300, 3250, 3150, 3050, 3350, 3280, 3120]

# combine lists into one list of tuples
data = [('Below 2000m', value) for value in altitude_band_1]
data += [('2000m-3000m', value) for value in altitude_band_2]
data += [('Above 3000m', value) for value in altitude_band_3]

# create a DataFrame
df = pd.DataFrame(data, columns=['Altitude Band', 'Avalanche Size (cubic m)'])

# create violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x='Altitude Band', y='Avalanche Size (cubic m)', data=df)

# add title
plt.title('Avalanche Sizes at Different Altitudes')

# set animated state of violins that contain the center point of the bounding box to True
plt.gca().violin_collection.set_animated(True)

# change color of violins that contain the center point of the bounding box to #cd8262
plt.gca().violin_collection.set_facecolor('#cd8262')

# show plot
plt.tight_layout()
plt.savefig("figure.png")