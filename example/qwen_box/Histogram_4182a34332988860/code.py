import matplotlib.pyplot as plt

# Data
income_pop = [20, 25, 32, 40, 45, 35, 38, 50, 55, 60, 45, 38, 42, 48, 55, 58, 
              62, 65, 50, 40, 36, 42, 49, 55, 58, 63, 70, 75, 80, 90, 85, 82, 
              78, 83, 88, 92, 98, 100, 98, 95, 92, 88, 85, 83, 80, 78, 75, 70, 
              66, 63, 58, 55, 52, 50, 48, 45, 42, 40, 36, 32, 28, 25, 20]

income_emp = list(range(30, 1010, 5))

# Plot for population income
plt.figure(figsize=(10,6))
plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))
plt.xlabel('Income in thousands of dollars')
plt.ylabel('Frequency')
plt.title('Income distribution of a population')
plt.grid(True)
plt.tight_layout()

# Stroke the bars that contain the center point of the bounding box
bbox = [40, 50, 60, 70, 80, 90, 100]
for i in range(len(bbox)):
    x = bbox[i]
    y = plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i]
    plt.bar(x, y, color='blue', linewidth=3, edgecolor='black', label='Population')
    plt.bar(x, y, color='blue', linewidth=3, edgecolor='black', label='Population', bottom=plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i-1], alpha=0.5)
    plt.bar(x, y, color='blue', linewidth=3, edgecolor='black', label='Population', bottom=plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i-1], alpha=0.5, hatch='///', linewidth=3)

# Apply a shadow below these bars with an offset of (3, 6) units
bbox = [40, 50, 60, 70, 80, 90, 100]
for i in range(len(bbox)):
    x = bbox[i]
    y = plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i]
    plt.bar(x, y, color='blue', linewidth=3, edgecolor='black', label='Population', bottom=plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i-1], alpha=0.5)
    plt.bar(x, y, color='blue', linewidth=3, edgecolor='black', label='Population', bottom=plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i-1], alpha=0.5, hatch='///', linewidth=3)
    plt.bar(x, y, color='blue', linewidth=3, edgecolor='black', label='Population', bottom=plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i-1], alpha=0.5, hatch='///', linewidth=3, bottom=plt.hist(income_pop, bins=range(min(income_pop), max(income_pop) + 10, 10))[0][i-1] + 3)

plt.legend()
plt.show()
plt.tight_layout()
plt.savefig("figure.png")