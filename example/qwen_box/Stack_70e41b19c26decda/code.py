import matplotlib.pyplot as plt

countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
soccer = [20, 15, 10, 12, 8]
basketball = [8, 10, 5, 6, 7]
cricket = [5, 3, 6, 8, 4]
tennis = [2, 3, 4, 1, 5]
baseball = [3, 2, 1, 4, 1.5]

plt.figure(figsize=(10,7))

plt.stackplot(countries, soccer, basketball, cricket, tennis, baseball, 
              colors=['blue', 'orange', 'green', 'red', 'purple'], 
              labels=['Soccer', 'Basketball', 'Cricket', 'Tennis', 'Baseball'])

bbox = plt.Bbox([[217, 187], [217 + 655, 187 + 298]])
plt.gca().add_patch(plt.Rectangle((bbox.x0, bbox.y0), bbox.width, bbox.height, fill=False, edgecolor='black', linewidth=4.4935, color='#58e236'))

plt.legend(loc='upper left')
plt.title('Number of sports fanatics by country')
plt.xlabel('Country')
plt.ylabel('Number of sports fanatics (in millions)')

plt.tight_layout()
plt.savefig("figure.png")