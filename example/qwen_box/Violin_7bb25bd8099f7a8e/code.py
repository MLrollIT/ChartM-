import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize Dataset
depth = ['5m', '10m', '15m', '20m', '25m', '30m', '35m', '40m', '45m', '50m']
seagrass_coverage = [20, 25, 22, 26, 30, 28, 32, 35, 30, 28]
kelp_coverage = [15, 18, 20, 22, 24, 26, 30, 28, 25, 20]
algae_coverage = [25, 25, 30, 32, 35, 40, 38, 36, 32, 30]
coral_coverage = [10, 12, 15, 18, 20, 22, 25, 23, 20, 18]

# Create DataFrame
df = pd.DataFrame({'Depth': depth*4, 
                   'Coverage': seagrass_coverage + kelp_coverage + algae_coverage + coral_coverage,
                   'Species': ['Seagrass']*len(depth) + ['Kelp']*len(depth) + ['Algae']*len(depth) + ['Coral']*len(depth)})

# Initialize Figure
plt.figure(figsize=(10, 6))

# Create Violin Plot
sns.violinplot(x='Species', y='Coverage', data=df, order=['Seagrass', 'Kelp', 'Algae', 'Coral'])

# Labeling
plt.title('Underwater Plant Distribution')
plt.xlabel('Plant Species')
plt.ylabel('Coverage Percentage')

# Set animated state of violins that contain the center point of the bounding box to False
plt.setp(plt.findobj(plt.gca(), 'violin'), animated=False)

# Set snap state of violins that are related to the center point of the bounding box to True
plt.setp(plt.findobj(plt.gca(), 'violin'), snap=True)

# Display Plot

plt.tight_layout()
plt.savefig("figure.png")