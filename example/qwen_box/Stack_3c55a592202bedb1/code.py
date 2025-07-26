import matplotlib.pyplot as plt
import numpy as np

# Weekly data for different age groups
weeks = [i for i in range(1, 27)]
age_groups = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '80+']
cases = [np.linspace(25, 50, 26),
         np.linspace(50, 70, 26),
         np.linspace(70, 100, 26),
         np.linspace(90, 120, 26),
         np.linspace(120, 150, 26),
         np.linspace(100, 70, 26),
         np.linspace(80, 60, 26),
         np.linspace(60, 40, 26),
         np.linspace(40, 25, 26)]

# Stack plot
plt.figure(figsize=(10, 7))
plt.stackplot(weeks, cases, labels=age_groups)

# Customize plot 
plt.xlabel('Weeks')
plt.ylabel('Number of Cases')
plt.title('Distribution of COVID-19 Cases Among Various Age Groups Over 6 Months')
plt.legend(loc='upper left')

# Hide the areas that contain the center point of the bounding box related to the target
plt.gca().collections[1].set_visible(False)

# Display plot
plt.tight_layout()
plt.savefig("figure.png")