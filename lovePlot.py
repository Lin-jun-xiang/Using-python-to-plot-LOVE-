import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(0, 20, 100, dtype=np.complex)
x = np.linspace(0, 2, 1500)
lx = np.linspace(-0.5, 0.5, 200)
plt.ion()

for ki in k:
    plt.clf()
    y = x ** (2 / 3) + 0.9 * np.sqrt(3.3 - x ** 2) * np.sin(ki * np.pi * x)
    if ki == k[-1]:
        plt.plot(x, y, color='red', linewidth=15)
        plt.plot(-x, y, color='red', linewidth=15)
        plt.scatter([-0.6, 0.6], [1.2, 1.2], color="black", s=150, zorder=3)
        plt.plot(lx, 1.8*lx**2, color='black', zorder=3)
        plt.xlim(-2, 2)
        plt.text(0, -1, "Love", fontsize=20, color='Pink', horizontalalignment ='center')
        plt.show()
        break
    plt.plot(x, y, color='red', linewidth=3)
    plt.plot(-x, y, color='red', linewidth=3)
    plt.xlim(-2, 2)
    plt.show()
    plt.pause(0.001)
