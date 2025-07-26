import matplotlib.pyplot as plt

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
expenses = [50, 40, 35, 45]
income = [30, 25, 20, 35]

plt.figure(figsize=(10,6))

plt.step(quarters, expenses, where='mid', label='Expenses')
plt.step(quarters, income, where='mid', label='Income')

plt.title('Comparison of Expenses and Income for each Quarter during COVID-19')
plt.ylabel('Amount in Thousands of Dollars')
plt.ylim(0, max(expenses+income)+10)
plt.legend()
plt.grid(True)

# plt.show()
plt.tight_layout()
plt.savefig("figure.png")