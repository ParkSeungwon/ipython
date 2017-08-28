import matplotlib.pyplot as plt
import numpy as np
xn = [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]
    
def F(w):
    r = 0
    for i in range(15): r += xn[i] * np.e**(-1j * w * (i-7))
    return r

w = np.arange(-2 * np.pi, 2*np.pi, 0.1);
Xw = F(w)
plt.subplot(211)
plt.plot(w, np.abs(Xw), w, np.angle(Xw))

Xw[:10] = 2
def inverse(n):
    return np.sum(Xw * np.e**(1j*w*n)) * 0.1 / 2 / np.pi

x = []
x_ = range(-10,10)
for i in x_:
    x.append(inverse(i).real)
plt.subplot(212)
plt.plot(x_, x)
plt.show()
