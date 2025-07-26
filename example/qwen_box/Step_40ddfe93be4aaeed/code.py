import matplotlib.pyplot as plt

continents = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia', 'Antarctica']
eruption_frequencies = [45, 32, 27, 38, 21, 13, 2]

plt.figure(figsize=(10, 6))
plt.step(continents, eruption_frequencies, where='mid', linestyle='dashdot', linewidth=2)
plt.title('Volcanic Eruptions Frequency Across Continents')
plt.xlabel('Continents')
plt.ylabel('Eruption Frequency')
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("figure.png")