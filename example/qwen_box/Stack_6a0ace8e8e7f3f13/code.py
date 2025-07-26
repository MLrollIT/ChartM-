import matplotlib.pyplot as plt

years = list(range(2010, 2020))

country_a = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
country_b = [15, 18, 20, 25, 30, 35, 40, 45, 50, 55]
country_c = [10, 12, 15, 20, 25, 30, 35, 40, 45, 50]
country_d = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
country_e = [25, 28, 30, 33, 35, 38, 40, 43, 45, 48]

plt.stackplot(years, country_a, country_b, country_c, country_d, country_e, labels=['Country A','Country B', 'Country C' , 'Country D', 'Country E'])

plt.legend(loc='upper left')
plt.ylabel('Percentage of renewable energy consumption')
plt.xlabel('Years')
plt.title('Renewable energy consumption: 2010-2019')

plt.tight_layout()
plt.savefig("figure.png")