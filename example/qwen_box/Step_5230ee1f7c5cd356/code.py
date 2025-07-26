import matplotlib.pyplot as plt
import numpy as np

# Aspects
aspects = ['Taste', 'Affordability', 'Cleanliness', 'Variety', 'Service']

# Ratings for McDonald's
ratings_mcd = {
    'Taste': [4.2, 4.4, 3.9, 4.3, 4.1],
    'Affordability': [3.8, 3.9, 4.1, 4.0, 3.7],
    'Cleanliness': [4.5, 4.3, 4.2, 4.4, 4.1],
    'Variety': [3.9, 4.2, 4.0, 4.1, 3.8],
    'Service': [4.0, 4.1, 4.3, 4.2, 4.0],
}

# Ratings for Burger King
ratings_bk = {
    'Taste': [4.1, 4.3, 3.8, 4.2, 4.0],
    'Affordability': [3.7, 3.8, 4.0, 3.9, 3.6],
    'Cleanliness': [4.4, 4.2, 4.1, 4.3, 4.0],
    'Variety': [3.8, 4.1, 3.9, 4.0, 3.7],
    'Service': [3.9, 4.0, 4.2, 4.1, 3.9],
}

# Create plot for each aspect
for aspect in aspects:
    plt.figure(figsize=(12, 5))
    
    plt.step(range(5), ratings_mcd[aspect], where='mid', label="McDonald's")
    plt.step(range(5), ratings_bk[aspect], where='mid', label='Burger King')
    
    plt.xticks(range(5), ['Rating 1', 'Rating 2', 'Rating 3', 'Rating 4', 'Rating 5'])
    plt.xlabel('Ratings')
    plt.ylabel('Average Rating')
    plt.title(f'{aspect} Rating Stair Plot')
    plt.grid(True)
    plt.legend()
    
    # Set animated state of the line that contains the center point of the bounding box to True
    for line in plt.gca().get_lines():
        if line.get_label() == "McDonald's":
            line.set_animated(True)
            line.set_zorder(11)
            line.set_alpha(0.5)
            line.set_linewidth(2)
            line.set_dashdotpattern([3.26, 2.76])
            break

plt.tight_layout()
plt.savefig("figure.png")