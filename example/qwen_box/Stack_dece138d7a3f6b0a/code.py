import matplotlib.pyplot as plt

# Age groups
ages = ['18-25 years', '26-35 years', '36-45 years', '46-55 years', '56-65 years']

# Stress levels per age group 
stress_levels_18_25 = [7, 6, 5, 6, 4]
stress_levels_26_35 = [6, 7, 4, 5, 3]
stress_levels_36_45 = [4, 5, 3, 4, 2]
stress_levels_46_55 = [3, 4, 2, 3, 1]
stress_levels_56_65 = [2, 3, 1, 2, 1]

# Plotting the data
plt.stackplot(ages, stress_levels_18_25, stress_levels_26_35, stress_levels_36_45, stress_levels_46_55, stress_levels_56_65, labels=['18-25','26-35','36-45','46-55','56-65'])

# Setting up labels and title
plt.xlabel('Age Group')
plt.ylabel('Stress Level')
plt.title('Impact of Daily Meditation on Stress Level by Age Group')
plt.legend()
plt.tight_layout()

# Adjusting the transparency and color of the area containing the center point of the bounding box
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.5
bbox[1] = 0.5
bbox[2] = 0.5
bbox[3] = 0.5
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='#236b04', alpha=0.66))

plt.savefig("Edit_figure.png")