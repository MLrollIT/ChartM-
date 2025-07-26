import matplotlib.pyplot as plt
import seaborn as sns

# Data 
inlet_velocity = [240, 245, 238, 250, 245, 242, 248, 252, 239, 246]
compressor_velocity = [300, 305, 308, 295, 310, 302, 298, 315, 303, 307]
combustion_chamber_velocity = [450, 445, 460, 455, 448, 465, 452, 458, 447, 462]
turbine_velocity = [400, 405, 398, 410, 415, 402, 395, 408, 412, 420]
exhaust_velocity = [600, 610, 605, 595, 620, 615, 602, 608, 625, 630]

# Prepare data for seaborn
data = [inlet_velocity, compressor_velocity, combustion_chamber_velocity, turbine_velocity, exhaust_velocity]
labels = ['Inlet', 'Compressor', 'Combustion Chamber', 'Turbine', 'Exhaust']

# Create violin plot
plt.figure(figsize=(10,8))
sns.violinplot(data=data)
plt.title('Fluid Flow Velocities in a Jet Engine')
plt.xlabel('Sections of Jet Engine')
plt.ylabel('Velocity (m/s)')
plt.xticks(range(5), labels)

# Set animated state of violins that contain the center point of the bounding box to False
bbox = plt.gca().get_position().get_points()
bbox[0] = [0.5, 0.5]
bbox[1] = [0.5, 0.5]
plt.gca().set_position(bbox)

# Update label of those violins to 'A new Label'
plt.legend(['A new Label'])

# show the plot
plt.tight_layout()
plt.savefig("figure.png")