import matplotlib.pyplot as plt

# Given data
sunlight_hours = [2, 4, 6, 8, 10, 12]  # Hours of sunlight exposure
mental_health_scores = [50, 55, 60, 65, 70, 75]  # Corresponding mental health scores

# Creating the step plot
plt.figure(figsize=(8, 6))
plt.step(sunlight_hours, mental_health_scores, where='mid')

# Setting the title and labels
plt.title('Daily Sunlight Exposure vs. Mental Health Scores in Winter')
plt.xlabel('Daily Sunlight Exposure in Hours')
plt.ylabel('Mental Health Scores')

# Setting the linestyle and marker edge color for the line containing the center point of the bounding box
plt.plot([8, 8], [60, 65], linestyle='dashdot', markeredgecolor='#81ee9b')

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")