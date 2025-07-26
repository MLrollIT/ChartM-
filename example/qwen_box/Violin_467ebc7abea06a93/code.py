import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Data
hours_of_sunlight = [6, 7, 7, 8, 7, 6, 8, 9, 9, 10, 7, 6, 8, 9, 9, 10, 8, 7, 8, 9, 10, 11, 7, 6, 8, 9, 9, 10, 8, 7, 6, 8, 9, 9, 10, 11]
plant_growth_and_yield = [10, 12, 14, 15, 11, 9, 16, 18, 20, 17, 13, 11, 14, 15, 17, 19, 15, 12, 14, 16, 19, 21, 13, 10, 13, 15, 17, 20, 15, 12, 10, 13, 15, 17, 20, 22]

# Ensure that the numpy arrays are of the same length
assert len(hours_of_sunlight) == len(plant_growth_and_yield), "The input arrays should have the same length!"

# Create a DataFrame
df = pd.DataFrame(list(zip(hours_of_sunlight, plant_growth_and_yield)), columns =['Hours of Sunlight', 'Plant Growth and Yield'])

# Create a violin plot
sns.violinplot(x = "Hours of Sunlight", y = "Plant Growth and Yield", data = df)

# Set the clip box for the violins that contain the center point of the bounding box
clip_box = plt.Bbox([[94, 188], [94 + 480, 188 + 141]])

# Show the plot
plt.title('Violin plot of the relation between hours of sunlight and plant growth and yield')
plt.tight_layout()
plt.savefig("figure.png")