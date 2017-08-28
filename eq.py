import numpy as np
import matplotlib.pyplot as plt

delta = 0.01
t = np.arange(0, 2*np.pi, delta)
x = []
y = []
x.append(0)
k=1
for i in t:
    x.append(np.sin(2 * np.pi * t))
    y.append(0.7 * x[k] + 0.3 * x[k-1])
    k += 1
plt.plot(x[1:],y)
plt.show()

