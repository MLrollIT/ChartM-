import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Creating a dictionary with keys as Shifts and Caffeine intake and values as Productivity levels
data_dict = {'Morning Shift (Low Caffeine)': [70, 60, 80, 75, 65, 55, 50, 45, 72, 68],
             'Morning Shift (High Caffeine)': [75, 70, 82, 77, 68, 58, 55, 50, 75, 72],
             'Afternoon Shift (Low Caffeine)': [60, 58, 70, 64, 50, 45, 40, 38, 65, 62],
             'Afternoon Shift (High Caffeine)': [68, 65, 75, 70, 58, 50, 48, 44, 70, 68],
             'Night Shift (Low Caffeine)': [55, 50, 62, 57, 45, 40, 38, 35, 60, 58],
             'Night Shift (High Caffeine)': [62, 60, 70, 65, 50, 45, 42, 40, 65, 62]}

# Converting the dictionary into a pandas DataFrame
prod_df = pd.DataFrame(data_dict)

# Melting the DataFrame to bring it in a proper format for the Violin Plot
prod_df_melted = pd.melt(prod_df, var_name="Shift & Caffeine intake", value_name="Productivity Levels")

# Plotting the Violin Plot using Seaborn
plt.figure(figsize=(10, 8))
sns.violinplot(x="Shift & Caffeine intake", y="Productivity Levels", data=prod_df_melted)
plt.title('Violin Plot of Productivity Levels for each Shift and Caffeine Intake')
plt.tight_layout()

# Get the bounding box coordinates of the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)

# Get the median line of the violins that contain the center point of the bounding box
median_lines = plt.gca().get_lines()[1::2]

# Change the median line color of the violins that contain the center point of the bounding box to #97dad0
for median_line in median_lines:
    median_line.set_color('#97dad0')

# Make the portion's box part invisible by setting its visibility to False
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='none', edgecolor='none', visible=False))

plt.savefig("Edit_figure.png")