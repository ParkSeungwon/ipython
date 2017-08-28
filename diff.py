import numpy as np
import matplotlib.pyplot as plt

delta = 0.01
t = np.arange(0, 10, delta)
z = []
y = []
k=0
z.append(3)
y.append(1)
for i in t:
   y.append(delta * z[k] + y[k])
   z.append(-delta * ( 2 * z[k] + y[k]) + z[k])
   k += 1
plt.plot(t,y[:-1])
plt.show()
