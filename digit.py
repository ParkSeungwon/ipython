import matplotlib.pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()
digits.images[0]

plt.imshow(digits.images[0], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
