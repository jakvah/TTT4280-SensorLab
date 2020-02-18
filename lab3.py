import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import importdata as ipd
import buggesmatteland as bml


[nomTp, rawData] = ipd.raspi_import(path,channels)

q = rawData[5:,3]
i = rawData[5:,4]

c = i + 1j*q
fft = np.fft.fft(c)

