import matplotlib.pyplot as plt
import numpy as np

im = plt.imread('buddha.jpg')
im2 = np.flipud(im)
plt.imshow(im2, origin='lower')
x = np.arange(1, 500, 0.01)
y = 100 * np.sin(x * 0.01) + 200
plt.plot(x, y)
plt.show()
