import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.plot([1,2,3,4],[0,0.7,0,0.3],'r--o')
plt.bar([1,2,3],[0.1,0.5,0.2])
#plt.pie([1,2,3])
plt.axis([0,7,0,1])
plt.grid()
plt.text(2, 0.5, 'What')
plt.xlabel('x axis label')
plt.ylabel('y axis lable')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()
