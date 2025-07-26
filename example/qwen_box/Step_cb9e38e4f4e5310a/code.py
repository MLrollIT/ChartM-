import matplotlib.pyplot as plt
import numpy as np

# Months 
Months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

# Sales data
sales_A = np.array([5000, 5200, 4800, 5500, 6200, 7100, 6900, 7300, 8000, 7800, 8200, 8500])
sales_B = np.array([3000, 3200, 3500, 3800, 4000, 4300, 4800, 4700, 5000, 5100, 5400, 5600])
sales_C = np.array([1500, 1600, 1800, 1900, 2200, 2400, 2600, 2800, 2900, 3000, 3200, 3300])

# Plotting data
plt.figure(figsize=(10,7)) # Change the figure size according to your requirement
plt.step(Months, sales_A, where='mid', label='Category A')
plt.step(Months, sales_B, where='mid', label='Category B')
plt.step(Months, sales_C, where='mid', label='Category C')

plt.xlabel('Months')
plt.ylabel('Sales in USD')
plt.title('Sales performance of various product categories')
plt.legend(loc='best')
plt.grid()

plt.tight_layout()
plt.savefig("figure.png")

# Fill the area below the step line that contains the center point of the bounding box with a gradient that starts with the color '#1c12a4' and transitions to '#d407c4'.
plt.fill_between(Months, sales_A, where=(sales_A >= 5000) & (sales_A <= 7000), color='#1c12a4', alpha=0.5)
plt.fill_between(Months, sales_B, where=(sales_B >= 4000) & (sales_B <= 5500), color='#d407c4', alpha=0.5)
plt.fill_between(Months, sales_C, where=(sales_C >= 2500) & (sales_C <= 3500), color='#1c12a4', alpha=0.5)
plt.fill_between(Months, sales_B, where=(sales_B >= 4000) & (sales_B <= 5500), color='#d407c4', alpha=0.5)
plt.fill_between(Months, sales_C, where=(sales_C >= 2500) & (sales_C <= 3500), color='#1c12a4', alpha=0.5)
plt.fill_between(Months, sales_B, where=(sales_B >= 4000) & (sales_B <= 5500), color='#d407c4', alpha=0.5)
plt.fill_between(Months, sales_C, where=(sales_C >= 2500) & (sales_C <= 3500), color='#1c12a4', alpha=0.5)
plt.fill_between(Months, sales_B, where=(sales_B >= 4000) & (sales_B <= 5500), color='#d407c4', alpha=0.5)
plt.fill_between(Months, sales_C, where=(sales_C >= 2500) & (sales_C <= 3500), color='#1c12a4', alpha=0.5)
plt.fill_between(Months, sales_B, where=(sales_B >= 4000) & (sales_B <= 5500), color='#d407c4', alpha=0.5)
plt.fill_between(Months, sales_C, where=(sales_C >= 2500) & (sales_C <= 3500), color='#1c12a4', alpha=0.5)
plt.fill_between(Months, sales_B, where=(sales_B >= 4000) & (sales_B <= 5500), color='#d407c4', alpha=0.5)
plt.fill_between(Month