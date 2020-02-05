import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

def raspi_import(path, channels=5):
    """
    Import data produced using adc_sampler.c.

    Parameters
    ----------
    path: str
        Path to file.
    channels: int, optional
        Number of channels in file.

    Returns
    -------
    sample_period: float
        Sample period
    data: ndarray, uint16
        Sampled data for each channel, in dimensions NUM_SAMPLES x NUM_CHANNELS.
    """

    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype=np.uint16)
        data = data.reshape((-1, channels))
    return sample_period, data


[Ts, data] = raspi_import("final_test.bin")
for i in range(5):
    
    d = data[5:,i]
    window = np.hamming(len(d))

    f = np.abs(sci.fft(d*window))
    
    f = f/len(f)
    freq = np.fft.fftfreq(n = len(f), d=32e-6)
    #spectrum = np.fft.fft(data, axis=0)  # takes FFT of all channels



    plt.subplot(2, 1, 1)
    plt.title("Time domain signal")
    plt.xlabel("Time [us]")
    plt.ylabel("Voltage")
    plt.plot(np.arange(len(d))*32e-6, d)

    plt.subplot(2, 1, 2)
    plt.title("Power spectrum of signal")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Power")
    plt.plot(freq, 10*np.log10(np.abs(f)**2)) # get the power spectrum
    plt.xlim(-1000,1000)

    """
    plt.plot(data[1:10000,i])
    plt.show()
    plt.plot(20*np.log10(abs(sci.fft(data[1:10000,i]))))
    """

    plt.show()


"""





plt.show()

"""


"""    
s = range(len(data[:,0]))
plt.plot(s, data[:,0], s, data[:,1])
plt.savefig("adc.png")"""
print(Ts)
