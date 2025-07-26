import matplotlib.pyplot as plt

# Age groups with corresponding data
data = {
    '18-24': [81, 84, 87, 89, 92],
    '25-34': [77, 79, 82, 85, 88],
    '35-44': [60, 64, 68, 72, 76],
    '45-54': [40, 43, 46, 49, 52],
    '55+': [26, 29, 32, 35, 38]
}

# Years on x-axis
years = [2016, 2017, 2018, 2019, 2020]

# Create step plot for each age group
for age_group, values in data.items():
    plt.step(years, values, where='post', label=age_group)

plt.xlabel('Years')
plt.ylabel('% of Internet Users Engaging with Social Media')
plt.title('Growth of Social Media Usage Among Different Age Groups (2016-2020)')
plt.legend(title='Age Groups:')
plt.grid(True)
plt.tight_layout()
plt.savefig("figure.png")