# Required Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Data
company_A = [12, 15, 20, 17, 14, 22, 19, 24, 28, 16, 18, 21, 23]
company_B = [10, 13, 18, 14, 17, 21, 19, 26, 22, 16, 20, 24, 25]
company_C = [9, 11, 16, 13, 15, 19, 18, 23, 20, 14, 17, 21, 22]
data = [company_A, company_B, company_C]
company_names = ['Company A', 'Company B', 'Company C']

# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# Create violinplot
sns.violinplot(data=data)

# Set x-axis labels
ax.set_xticklabels(company_names)

# Set title and labels
plt.title('Ride-Sharing Trip Duration Analysis')
plt.xlabel('Companies')
plt.ylabel('Trip Duration in Minutes')

# Modify the label of the violin that contains the center point of the bounding box
ax.set_xlabel('A new Label')

# Set the visibility of the box part to false
ax.set_box_visible(False)

# Show plot
plt.tight_layout()
plt.savefig("figure.png")