import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.io import loadmat
import scipy.signal as signal
import scipy.fftpack

# load the file
matfile = loadmat('spectral_codeChallenge.mat')

signalValues = matfile['signal'][0]
signalTimes = matfile['time'][0]  # signal with morlet wavelet applied
srate = matfile['srate'][0][0]
plt.figure(0)
plt.plot(signalTimes, signalValues)


signalX = scipy.fftpack.fft(signalValues)
signalAmp = 2 * np.abs(signalX) / len(signalX)


plt.figure(1)
plt.plot(signalTimes, signalValues, label='Original')
plt.plot(signalTimes, np.real(scipy.fftpack.ifft(signalX)), 'red', label='IFFT reconstructed')
# plt.plot(signalTimes, np.real(scipy.fftpack.ifft(signalX)), 'ro', label='IFFT reconstructed')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time domain')
plt.legend()
plt.show()
