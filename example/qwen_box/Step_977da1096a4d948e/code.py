import matplotlib.pyplot as plt

# Create lists of data
age_groups = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
percentages = [30, 40, 35, 20, 15, 10]

# Plot the step chart
plt.figure()
plt.step(age_groups, percentages, where='mid', color='blue', alpha=0.63)
plt.scatter([age_groups[5]], [percentages[5]], color='black', marker='o', s=16.38)

plt.title('Impact of Social Media on Voter Behavior Across Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Percentage of Voters Influenced by Social Media (%)')
plt.grid(True)

# plt.show()
plt.tight_layout()
plt.savefig("figure.png")