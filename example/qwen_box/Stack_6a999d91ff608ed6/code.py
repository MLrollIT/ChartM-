import matplotlib.pyplot as plt

celebrities = ['Celebrity 1', 'Celebrity 2', 'Celebrity 3', 'Celebrity 4', 'Celebrity 5']
Instagram_followers = [10, 25, 30, 15, 20]
Twitter_followers = [5, 12, 18, 8, 10]
YouTube_subscribers = [3, 8, 10, 5, 7]

plt.figure(figsize=(10, 6))

plt.stackplot(celebrities, Instagram_followers, Twitter_followers, YouTube_subscribers, 
              colors=['blue', 'orange', 'green'], labels=['Instagram','Twitter','YouTube'])

plt.legend(loc='upper left')

plt.ylabel('No. of followers/subscribers (M)')
plt.title('Social media following of top celebrities')


plt.tight_layout()
plt.savefig("figure.png")