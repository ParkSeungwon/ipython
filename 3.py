import matplotlib.pyplot as plt
import numpy as np

xn = np.zeros(10);
for i in range(10): xn[i] = (1./3.)**i

def F(w):
    r = 0
    for i in range(10): r += xn[i] * np.e**(-1j * w * i)
    return r

w = np.arange(0, 2*np.pi, 0.1);
plt.subplot(211)
plt.plot(w, np.abs(F(w)), w, np.angle(F(w)))

def inverse(n):
    return np.sum(F(w) * np.e**(1j*w*n)) * 0.1 / 2 / np.pi
x = []
for i in range(10): 
    r = inverse(i)
    print r,
    x.append(r.real)
plt.subplot(212)
plt.plot(x)
plt.show()
    
