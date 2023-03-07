from random import randint
import math
import matplotlib.pyplot as plt
import numpy as np

#print(randint(1, 6))
#print(math.log10(100))
#print(math.exp(2))


def plotDiagram():
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints)
    plt.show()