import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
step_counts = [4564, 5678, 3845, 4987, 5321, 4210, 5874, 3765, 5123, 4980, 
               5439, 5120, 4625, 5890, 5745, 5123, 5980, 4398, 5214, 5534, 
               6890, 7412, 6543, 7089, 6545, 7120, 6874, 7210, 6880, 7678]

# Categories
steps_types = ['Urban'] * 10 + ['Suburban'] * 10 + ['Rural'] * 10

# Creating DataFrame
df = pd.DataFrame()
df['Area'] = steps_types
df['Average Daily Steps'] = step_counts

# Plotting
plt.figure(figsize=(10,6))
sns.violinplot(x='Area', y='Average Daily Steps', data=df, inner='point')
plt.title('Average Daily Steps Taken by Individuals Living in Different Areas')
plt.tight_layout()

# Get the bounding box of the center point of the violin
bbox = plt.gca().get_position()

# Set the rasterized state of the violin to True
plt.gca().violin_collection.set_rasterized(True)

# Change the transform of the violin to the axes' coordinate system
plt.gca().violin_collection.set_transform(plt.gca().transAxes)

plt.savefig("Edit_figure.png")