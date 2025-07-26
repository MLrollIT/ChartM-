import matplotlib.pyplot as plt
import seaborn as sns

# data
profitability = {
    "Manufacturing": [10, 12, 15, 18, 20, 25, 28],
    "Technology": [5, 8, 12, 15, 18, 20, 25],
    "Agriculture": [2, 4, 6, 10, 12, 15, 18],
    "Services": [15, 18, 22, 25, 30, 35, 40],
    "Retail": [8, 10, 12, 15, 20, 25, 30],
}

# preparing data for plot
labels, data = [*zip(*profitability.items())]  # 'transpose' items to parallel key, value lists

# or backwards compatable    
labels, data = profitability.keys(), profitability.values()

plt.figure(figsize=(10,6))
plt.boxplot(data)
plt.xticks(range(1, len(labels) + 1), labels)
plt.title('Profitability by industry')
plt.xlabel('Industry')
plt.ylabel('Profitability (%)')
plt.savefig('Edit_figure.png')

plt.tight_layout()
plt.savefig("Edit_figure.png")