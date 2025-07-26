import matplotlib.pyplot as plt

years = list(range(2010, 2020))
germany_rates = [1.4, 1.5, 1.6, 1.4, 1.3, 1.5, 1.7, 1.6, 1.5, 1.4]
japan_rates = [1.2, 1.1, 1.0, 0.9, 0.8, 0.8, 0.9, 0.9, 0.9, 0.8]
usa_rates = [2.0, 2.1, 2.3, 2.2, 2.0, 2.1, 2.0, 1.9, 1.8, 1.7]
brazil_rates = [1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.3, 1.2, 1.2, 1.1]
india_rates = [2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 2.0, 1.9, 1.8, 1.7]

plt.figure(figsize=(10, 7))
plt.stackplot(years, germany_rates, japan_rates, usa_rates, brazil_rates, india_rates, labels=['Germany', 'Japan', 'USA', 'Brazil', 'India'])
plt.legend(loc='upper right')
plt.title('Fertility Rate Comparison')
plt.xlabel('Years')
plt.ylabel('Fertility Rates')

bbox = plt.gca().get_position().get_points()
bbox[0] = 0.55
bbox[1] = 0.55
bbox[2] = 0.65
bbox[3] = 0.65

plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], fill=False, linestyle='dotted', color='#5f322c'))

plt.tight_layout()
plt.savefig("figure.png")