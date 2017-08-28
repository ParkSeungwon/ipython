import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi, np.pi, 201);
fn = [0] * 201;

for N in np.arange(1, 100, 2):
    fn += 4 / np.pi * np.sin(N * t) / N;

plt.plot(t, fn)
plt.show()
