# Straight up takk til Bjørn :=)

import numpy
import matplotlib.pyplot as gfx
import scipy.signal as signal



def import_data(path, channels=2):
    with open(path, 'r') as fid:
        sample_period = numpy.fromfile(fid, count=1, dtype=float)[0]
        data = numpy.fromfile(fid, dtype=numpy.uint16)
        data = data.reshape((-1, channels))
    return sample_period, data



def combine_iq(data):
    iq_data = []

    for i in data:
        iq_data.append(i[0] + 1j*i[1])
    
    return iq_data



def findPeak(fft_data, fft_axis):
    # Find the top peak
    i = numpy.argmax(fft_data)

    # Find the corresponding frequency
    peak_frequency = fft_axis[i]

    return peak_frequency



def plot(sample_period, data):
    # Change sample period to microseconds
    sample_period *= 1e-6

    # Get the size of the array
    number_of_samples = data.shape[0]

    data = combine_iq(data)

    # Take the FFT
    fft_axis = numpy.fft.fftfreq(n = number_of_samples, d = sample_period)
    fft_data = numpy.fft.fft(data, axis = 0)
    doppler_frequency = findPeak(fft_data, fft_axis)

    # Multiply the doppler frequency with the wavelength to get the speed
    speed = (doppler_frequency * 3e8)/(2*24.13e7)
    
    # Direction
    direction = 0

    if (speed < 0):
        speed *= -1
        direction = 0
    else:
        direction = 1

    print("The doppler frequency is:\t", doppler_frequency, " Hz")
    print("Estimated speed is:\t\t", speed, " cm/s")
    if (direction == 0):
        print("Direction:\t\t\t Negative")
    else:
        print("Direction:\t\t\t Positive")

    # Plot the power spectrum
    gfx.subplot(2, 1, 2)
    gfx.xlabel("Frequency [Hz]")
    gfx.ylabel("Power [dB]")
    gfx.xlim(-500, 500)
    gfx.ylim(-1, 400)
    gfx.plot(fft_axis, 20*numpy.log(numpy.abs(fft_data)), color='blue') # get the power spectrum



def remove_dc(data):
    return signal.detrend(data, axis=0)


def strip_data(data):
    
    # Strip data function

    return data


def main():

    # Set the window title
    fig = gfx.gcf()
    fig.canvas.set_window_title('Radar plot')

    print("\n---------------------------------------------\n")

    # Import data from bin file
    sample_period, data = import_data('radarData/m4_0_6.bin')

    # Optional remove first n samples
    data = strip_data(data) # Does nothing atm
    data = remove_dc(data)  # removes DC component for each channel

    # Plot the data and the power spectrum
    #plot(sample_period, data)

    # Generate time axis
    num_of_samples = data.shape[0]  # returns shape of matrix
    t = numpy.linspace(start=0, stop=num_of_samples*sample_period, num=num_of_samples)

    # Generate frequency axis and take FFT
    freq = numpy.fft.fftfreq(n=num_of_samples, d=sample_period)
    spectrum = numpy.fft.fft(data, axis=0)  # takes FFT of all channels

    print("---------------------------------------------\n")

    # Plot the results in two subplots
    # NOTICE: This lazily plots the entire matrixes. All the channels will be put into the same plots.
    # If you want a single channel, use data[:,n] to get channel n
    gfx.subplot(2, 1, 1)
    gfx.xlabel("Time [us]")
    gfx.ylabel("Voltage")

    gfx.plot(t, data[:, 0], color='blue')
    gfx.plot(t, data[:, 1], color='green')

    

    # The three lines below can be uncommented to run the plot in full screen

    #window_manager = gfx.get_current_fig_manager()
    #window_manager.resize(*window_manager.window.maxsize())
    #window_manager.window.wm_geometry("-0+0")
    gfx.show()



main()