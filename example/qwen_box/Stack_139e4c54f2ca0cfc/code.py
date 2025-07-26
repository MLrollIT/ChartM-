import matplotlib.pyplot as plt

# Time points
x = [0, 1, 2, 3, 4]

# Concentrations of reactants A, B and product C
y1 = [20, 18, 15, 10, 5]
y2 = [15, 14, 12, 8, 5]
y3 = [0, 5, 10, 15, 20]

# Make the stack plot
plt.figure(figsize=(10,7))
plt.stackplot(x, y1, y2, y3, labels=['Reactant A','Reactant B','Product C'], alpha=0.5 )

# Legend to the upper left corner
plt.legend(loc='upper left')

# Titles and labels
plt.title('Chemical Reactions in 3D Space Over Time')
plt.xlabel('Time intervals')
plt.ylabel('Concentration')

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")