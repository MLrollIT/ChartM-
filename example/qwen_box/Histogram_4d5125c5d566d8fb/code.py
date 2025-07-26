# importing necessary libraries
import matplotlib.pyplot as plt

# Satisfaction levels (mid-point of each range)
satisfaction_levels = [10, 30, 50, 70, 90]

# Number of employees in each satisfaction level
employees = [10, 25, 50, 75, 30]

plt.figure(figsize=(10, 6)) # Set the figure size
plt.bar(satisfaction_levels, employees, width=15, color='skyblue', edgecolor='black') # Plot the data
plt.title('Employee Satisfaction Levels Over Time') # Set the plot title
plt.xlabel('Satisfaction Level (%)') # Set the x-axis label
plt.ylabel('Number of Employees') # Set the y-axis label

# Customize x-axis ticks
plt.xticks([10, 30, 50, 70, 90], ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%'])

# Customize the linestyle of the bars that contain the center point of the bounding box
plt.bar([50], [75], width=15, color='skyblue', edgecolor='black', linestyle='--')

# plt.show()
plt.tight_layout()
plt.savefig("Edit_figure.png")