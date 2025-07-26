import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [1, 3, 5, 6, 8, 9, 7, 6, 5, 4]
y2 = [10, 20, 30, 25, 35, 45, 40, 35, 30, 25] 

# Plot
plt.figure(figsize=(10, 6))
plt.step(x, y1, where='mid', label='Social Media Engagement (in thousands)')
plt.step(x, y2, where='mid', label='Sales Conversions (in hundreds)')

# Title and labels
plt.title('Stair plot: Social Media Engagement & Sales Conversion')
plt.xlabel('Duration of Campaign (in segments)')
plt.ylabel('Metrics')
plt.legend(loc='best')

plt.grid(True)

plt.tight_layout()
plt.savefig("figure.png")