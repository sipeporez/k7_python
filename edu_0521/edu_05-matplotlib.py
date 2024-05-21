import matplotlib.pyplot as plt

# import random

squares = [i**2 for i in range(-100, 100)]
# squares = [random.randint(1, 100) for _ in range(10000)]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
