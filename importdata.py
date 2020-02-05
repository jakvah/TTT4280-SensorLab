import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
from scipy import signal
def raspi_import(path, channels):
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



def preProc(data, upSampleFactor):
    length = len(data[:,0])
    mic = np.zeros((length,5))
    mic = signal.detrend(data[:,:5], axis=0, type="constant")
    
    if(upSampleFactor != 1):
        mic = signal.resample(mic, upSampleFactor*length, axis=0)
    
    # Might also add filter here
    
    return mic
