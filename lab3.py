import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import importdata as ipd
import buggesmatteland as bml
from scipy import signal as sig

path = 'dassli.bin'
channels = 5
[nomTp, rawData] = ipd.raspi_import(path,channels)

q = rawData[5:,3]
i = rawData[5:,4]


q_d = sig.detrend(q,type="constant")
i_d = sig.detrend(i,type="constant")



c = q_d + 1j*i_d
fft = np.fft.fft(c)

plt.subplot(5, 1, 1)
plt.title("fft")
plt.xlabel("Sample")
plt.ylabel("gutta")
plt.plot(np.arange(len(fft))*32e-6, fft)
plt.show()




