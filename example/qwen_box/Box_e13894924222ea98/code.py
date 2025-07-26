import matplotlib.pyplot as plt

robot_distances = [
    [250, 275, 300, 325, 350, 375, 400],
    [200, 225, 250, 275, 300, 325, 350],
    [180, 200, 220, 240, 260, 280, 300],
    [300, 320, 340, 360, 380, 400, 420],
    [150, 175, 200, 225, 250, 275, 300]
]

plt.figure(figsize=(10, 6))
plt.boxplot(robot_distances, labels=["Robot 1", "Robot 2", "Robot 3", "Robot 4", "Robot 5"], patch_artist=True)
plt.xlabel('Robots')
plt.ylabel('Distance Traveled (m)')
plt.title('Box Plot of Robot Swarm Movement Analysis')
plt.savefig('figure.png')

plt.tight_layout()
plt.savefig("figure.png")