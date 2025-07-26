import matplotlib.pyplot as plt

# Data points for bacterial growth rates in varying environments
time_hours = [0, 4, 8, 12, 16, 20]
growth_25C = [0.2, 0.5, 0.8, 1.1, 1.3, 1.6]
growth_30C = [0.4, 0.7, 1.0, 1.3, 1.6, 1.9]
growth_37C = [0.6, 0.9, 1.2, 1.5, 1.8, 2.1]

plt.figure(figsize=(12, 8))
plt.boxplot([growth_25C, growth_30C, growth_37C], labels=['25°C', '30°C', '37°C'])
plt.xlabel('Temperature Levels')
plt.ylabel('Bacterial Growth Rate (OD600 units)')
plt.title('Box Plot of Bacterial Growth in Varying Environments')
plt.boxplot([growth_25C, growth_30C, growth_37C], labels=['25°C', '30°C', '37°C'], positions=[1, 2, 3], widths=0.5, patch_artist=True, showmeans=True, meanprops=dict(marker='o', markerfacecolor='black', markersize=10), meanline=True, medianprops=dict(linewidth=2.11, color='black'), boxprops=dict(linewidth=2.11, color='black'), capprops=dict(linewidth=2.11, color='black'), whiskerprops=dict(linewidth=2.11, color='black'), flierprops=dict(marker='o', markerfacecolor='black', markersize=10), showfliers=False)
plt.tight_layout()
plt.savefig("figure.png")