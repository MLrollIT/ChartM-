import matplotlib.pyplot as plt

# Quantum states
states = ['State A', 'State B', 'State C', 'State D', 'State E']

# Entanglement strengths for each state
entanglement_strengths = {
    'State A': [0.8, 0.9, 0.7, 0.6, 0.8],
    'State B': [0.5, 0.6, 0.4, 0.3, 0.2],
    'State C': [0.9, 0.8, 0.7, 0.6, 0.8],
    'State D': [0.3, 0.4, 0.2, 0.1, 0.3],
    'State E': [0.7, 0.6, 0.5, 0.4, 0.6]
}

# Create plot
fig, ax = plt.subplots()

for state in states:
    ax.step(range(len(entanglement_strengths[state])), entanglement_strengths[state], where='mid', label=state)

# Set the plot labels
plt.xlabel('Quantum States')
plt.ylabel('Entanglement Strength')
plt.title('Quantum Entanglement in TimeSpace Theory')

# Add a legend
plt.legend()

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")