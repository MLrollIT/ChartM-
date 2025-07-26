import matplotlib.pyplot as plt

decades = ['1950s', '1960s', '1970s', '1980s', '1990s', '2000s']

vintage = [30, 20, 10, 5, 10, 15]
glamorous = [20, 40, 30, 30, 40, 30]
casual = [10, 30, 40, 10, 20, 20]
chic = [40, 10, 20, 55, 30, 35]

plt.figure(figsize=(10,6))

plt.stackplot(decades, vintage, glamorous, casual, chic,
              labels=['Vintage', 'Glamorous', 'Casual', 'Chic'],
              colors=['#6d904f', '#fc4f30', '#008fd5', '#e5ae38'], alpha=0.7)

plt.legend(loc='upper left')

plt.title('Fashion Trends over Six Decades')
plt.xlabel('Decade')
plt.ylabel('Percentage')

plt.tight_layout()
plt.savefig("figure.png")