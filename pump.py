import numpy as np
import matplotlib.pyplot as plt

k=0
delta=0.01
t = np.arange(0, 1000, delta)
h = []
h.append(10)
A = 10
qmi = 25
r = 2
R = 5
for i in t:
    h.append(delta / A * (qmi/r - h[k]/R) + h[k])
    k += 1
plt.plot(t, h[:-1])
plt.show()

