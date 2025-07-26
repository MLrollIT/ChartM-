import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('data.csv')

# Create the violinplot
sns.violinplot(data=data)

# Set the title and labels
plt.title('Distribution of Stellar Mass Densities in Different Star Formation Regions')
plt.xlabel('Star Forming Regions')
plt.ylabel('Log(Stellar Mass Density) [Solar Masses / Square Parsec]')
plt.xticks(range(len(data['Region'].unique())), data['Region'].unique())

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")