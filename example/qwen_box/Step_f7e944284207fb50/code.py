import matplotlib.pyplot as plt

# Data
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65']
popularity_scores = [60, 75, 80, 70, 55]

# Create stair plot
plt.step(age_groups, popularity_scores)

# Set plot title and labels
plt.title('Popularity of Floral Fragrances Among Different Age Groups')
plt.xlabel('Age Groups')
plt.ylabel('Popularity Score')

# Show plot
plt.tight_layout()
plt.savefig("figure.png")