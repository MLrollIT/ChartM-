import matplotlib.pyplot as plt
import numpy as np

# Define the age ranges as a list of strings
age_ranges = ['18-24', '25-34', '35-44', '45-54', '55-64']

# Define the percentage of individuals with a mental health disorder
mental_health_percentages = [14, 16, 12, 10, 8]

# Define the percentage of individuals with alcohol dependency or abuse
alcohol_percentages = [8, 10, 6, 5, 4]

# Define the number of age ranges
n_ranges = len(age_ranges)

# Set the figure size
plt.figure(figsize=(10,6))

# Plot the mental health percentages
plt.plot(np.arange(n_ranges), mental_health_percentages, drawstyle='steps-mid', label='Mental Health Disorders', color='#f93792', linewidth=2.73, linestyle='-', marker='o', markersize=10, markerfacecolor='none', markeredgecolor='#1a16d2')

# Plot the alcohol percentages
plt.plot(np.arange(n_ranges), alcohol_percentages, drawstyle='steps-mid', label='Alcohol Dependency or Abuse', color='orange', linewidth=2.73, linestyle='-', marker='o', markersize=10, markerfacecolor='none', markeredgecolor='orange')

# Set the x-ticks to be the age ranges
plt.xticks(np.arange(n_ranges), age_ranges)

# Add labels and title
plt.xlabel('Age Range')
plt.ylabel('Percentages (%)')
plt.title('Mental Health Disorders and Alcohol Dependency or Abuse by Age Range')

# Add legend
plt.legend()

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")