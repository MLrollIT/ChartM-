import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('data.csv')

# Create a new figure
plt.figure(figsize=(10, 6))

# Create a violin plot
sns.violinplot(data=data)

# Assign labels to the x-axis
plt.xticks([0, 1, 2], ['Wild-Type', 'Mutant A', 'Mutant B'])

# Set the title and labels
plt.title('Violin plot of RMSD values')
plt.xlabel('Simulation scenario')
plt.ylabel('RMSD values (in angstroms)')

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")