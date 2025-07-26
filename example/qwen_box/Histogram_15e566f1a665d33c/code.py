import matplotlib.pyplot as plt

# Cloud cover percentage ranges
x = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%']

# Frequency of cloud cover percentages
y = [25, 32, 38, 45, 50, 48, 42, 35, 28, 20]

plt.figure(figsize=(10, 6))

# Plotting the data using a histogram
plt.bar(x, y, color='skyblue', edgecolor='black')

plt.xlabel('Cloud Cover Percentage', fontsize=12)
plt.ylabel('Frequency of Cloud Cover Percentage', fontsize=12)
plt.title('Distribution of Cloud Coverage Percentages Observed in Satellite Images', fontsize=15)
plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()

# Get the center point of the bounding box
center_point = (40, 50)

# Find the bar that contains the center point
for i, bar in enumerate(plt.gca().patches):
    if bar.get_x() <= center_point[0] <= bar.get_x() + bar.get_width():
        bar.set_animated(False)

plt.savefig("figure.png")