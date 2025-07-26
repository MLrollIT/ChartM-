import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
depth = [0, 5, 10, 15, 20, 25, 30]
temperature = {
    '0': [25, 25, 26, 26, 26.5, 26, 25.5],
    '5': [24, 24.5, 25, 25.5, 26, 25.5, 25],
    '10': [23, 23.5, 24, 24.5, 24.5, 24, 23.5],
    '15': [22, 22.5, 23, 23, 23, 22.5, 22],
    '20': [21, 21, 21.5, 22, 22, 21.5, 21],
    '25': [20, 20.5, 20.5, 20.5, 20.5, 20, 19.5],
    '30': [19, 19, 19, 19, 19, 18.5, 18]
}

# Convert the data into a pandas dataframe
df = pd.DataFrame(data=temperature)

# Change the dataframe from wide to long form
df = df.melt(var_name='Depth (in meters)', value_name='Temperature (in degrees Celsius)')

# Convert Depth from string to integer
df['Depth (in meters)'] = df['Depth (in meters)'].astype(int)

# Plot the data using a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Depth (in meters)', y='Temperature (in degrees Celsius)', data=df)
plt.title('Temperature Variations at Different Depths of an Underwater Cave System Over a 24-Hour Period')
plt.tight_layout()

# Get the bounding box of the violin plot
bbox = plt.gca().get_position()

# Create a new figure with the same size as the original figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data using a violin plot
sns.violinplot(x='Depth (in meters)', y='Temperature (in degrees Celsius)', data=df, ax=ax)
plt.title('Temperature Variations at Different Depths of an Underwater Cave System Over a 24-Hour Period')
plt.tight_layout()

# Get the bounding box of the violin plot
bbox = ax.get_position()

# Hide the median line of the violin that contain the center point of the bounding box
ax.set_box_aspect(1)
ax.set_xlim([0, 30])
ax.set_ylim([18, 27])
ax.set_xticks(range(0, 31, 5))
ax.set_yticks(range(18, 28, 2))
ax.set_xlabel('Depth (in meters)')
ax.set_ylabel('Temperature (in degrees Celsius)')
ax.set_title('Temperature Variations at Different Depths of an Underwater Cave System Over a 24-Hour Period')
ax.set_position(bbox)

# Save the figure
plt.savefig("figure.png")