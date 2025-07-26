import matplotlib.pyplot as plt

# Data points for survival outcomes and counts
survival_outcomes = ['Survived', 'Did not survive']
counts = [342, 549]

# Plotting the histogram
fig, ax = plt.subplots()
ax.bar(survival_outcomes, counts, color=['green','red'])

# Labeling the axes
plt.xlabel('Survival Outcomes')
plt.ylabel('Count')

# Setting the title
plt.title('Survival Rate of Shipwreck Passengers')

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")

# Modify the object in the chart
for bar in ax.patches:
    if bar.get_facecolor() == '#ef21c5':
        bar.set_edgecolor('#ef21c5')
        bar.set_linewidth(2.95)