import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import numpy as np
from scipy.fftpack import fft

M=501
hM1 = 251
hM2 = 250

fs, x = read('app.wav')
x1 = x[5000:5000+M] * np.hamming(M)

N = 1024
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer)
mX = 20 * np.log10(abs(X))
pX = np.unwrap(np.angle(X))

#plt.plot(fftbuffer)
#plt.plot(mX[:512])
plt.plot(pX[:512])
plt.show()
