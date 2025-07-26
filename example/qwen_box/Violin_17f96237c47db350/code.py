import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define the age groups and corresponding average daily screen time data
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
screen_times = [[5.6, 6.2, 5.8, 6.1, 5.9, 6.5, 5.7, 6.0],
                [6.8, 7.2, 6.5, 6.9, 7.3, 6.7, 7.1, 6.6],
                [7.5, 8.1, 7.7, 7.3, 8.0, 7.8, 7.9, 7.6],
                [8.3, 7.9, 8.2, 8.5, 8.1, 7.5, 8.4, 7.8],
                [6.9, 7.3, 7.6, 7.0, 7.2, 7.4, 7.1, 7.5],
                [4.5, 4.2, 4.9, 4.8, 4.3, 4.6, 4.7, 4.4]]

# Prepare data for violin plot
data = []
for group, times in zip(age_groups, screen_times):
    for time in times:
        data.append([group, time])

# Convert the data to pandas DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=['Age Group', 'Average Daily Screen Time'])

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Age Group', y='Average Daily Screen Time', data=df)

# Set the animated state of the violins that contain the center point of the bounding box to False
bbox = plt.gca().get_position().get_points()
bbox[0] = (bbox[0][0], 0.5)
bbox[1] = (bbox[1][0], 0.5)
plt.gca().set_position(bbox)

# Make the box part of this violin invisible by setting its visibility to False
plt.gca().violinplot([df['Average Daily Screen Time']], showbox=False, showcaps=False)

# Display the plot
plt.title('Smartphone Usage Pattern Among Different Age Groups')
plt.tight_layout()
plt.savefig("figure.png")