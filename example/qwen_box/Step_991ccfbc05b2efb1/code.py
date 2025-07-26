import matplotlib.pyplot as plt
import numpy as np

# Creating the data
companies = ["Company A", "Company B", "Company C", "Company D", "Company E"]
male_salaries = [90000, 95000, 100000, 92000, 88000]
female_salaries = [80000, 85000, 90000, 82000, 78000]

x = np.arange(len(companies))

# Creating the plot
fig, ax = plt.subplots()

ax.step(x, male_salaries, label='Male', where='mid')
ax.step(x, female_salaries, label='Female', where='mid')

# Customizing the plot
ax.set_xlabel("Companies")
ax.set_ylabel("Average Salary (in USD)")
ax.set_title("Gender Pay Gap in the Tech Industry")
ax.set_xticks(x)
ax.set_xticklabels(companies)
ax.legend()

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")