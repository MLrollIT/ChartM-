import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
coffee_consumption = ['No coffee', 'Moderate coffee', 'High coffee']
accidents_no_coffee = [1, 0, 1, 2, 1]
accidents_moderate_coffee = [2, 1, 2, 3, 2]
accidents_high_coffee = [5, 4, 3, 6, 5]

# Prepare data for plotting
data = {
    'Coffee Consumption': (
        ['No Coffee'] * len(accidents_no_coffee) + 
        ['Moderate Coffee'] * len(accidents_moderate_coffee) + 
        ['High Coffee'] * len(accidents_high_coffee)
    ),
    'Frequency of Accidents': accidents_no_coffee + accidents_moderate_coffee + accidents_high_coffee
}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Coffee Consumption', y='Frequency of Accidents', data=df)
plt.title('Relationship Between Coffee Consumption and Workplace Accidents Among Night Shift Workers')
plt.xlabel('Coffee Consumption Levels')
plt.ylabel('Frequency of Accidents (per month)')
plt.tight_layout()
plt.savefig("figure.png")

# Modify the face color of the violins that contain the center point of the bounding box to #af0e61
violin = plt.gca().violinplot(data, positions=[2], showmeans=True, showextrema=False)
for body in violin['bodies']:
    body.set_facecolor('#af0e61')