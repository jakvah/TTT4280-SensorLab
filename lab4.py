import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import buggesmatteland as bml

pulseData = np.loadtxt("film5.txt")
pulseData = sig.detrend(pulseData,axis = 0)

# -------------------- Time signal ------------------- #

red = pulseData[:,0]
green = pulseData[:,1]
blue = pulseData[:,2]

plt.subplot(321)
plt.title("Red time signal")
plt.plot(red,"r")


plt.subplot(325)
plt.title("Green time signal")
plt.plot(green,"g")

plt.subplot(323)
plt.title("Blue time signal")
plt.plot(blue,"b")

# -------------------- Moving average ------------------- #

redMvAvg = bml.movingAverage(red,10)
blueMvAvg = bml.movingAverage(blue,10)
greenMvAvg = bml.movingAverage(green,10)

plt.subplot(322)
plt.title("Red time signal moving average")
plt.plot(redMvAvg,"r")


plt.subplot(326)
plt.title("Green time signal mv avg")
plt.plot(greenMvAvg,"g")

plt.subplot(324)
plt.title("Blue time signal mv avg")
plt.plot(blueMvAvg,"b")

plt.show()



# -------------------- FFT ------------------- #

fft_red = np.fft.rfft(redMvAvg,axis = 0)
fft_green = np.fft.rfft(greenMvAvg,axis = 0)
fft_blue = np.fft.rfft(blueMvAvg,axis = 0)

plt.subplot(3,1,1)
plt.title("Red FFT")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(fft_red,"r")

plt.subplot(3,1,2)
plt.title("Green FFT")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(fft_green,"g")

plt.subplot(3,1,3)
plt.title("Blue FFT")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(fft_blue,"b")
plt.show()

# -------------------- AutoCorr ------------------- #

auto_red_temp = np.correlate(redMvAvg,redMvAvg,"full")
auto_green_temp = np.correlate(greenMvAvg,greenMvAvg,"full")
auto_blue_temp = np.correlate(blueMvAvg,blueMvAvg,"full")

# Can't work with np arrays for some reason...
autoRed = []
for j in auto_red_temp:
    autoRed.append(j)
autoGreen = []
for j in auto_green_temp:
    autoGreen.append(j)
autoBlue = []
for j in auto_blue_temp:
    autoBlue.append(j)


plt.subplot(3,1,1)
plt.title("Red auto correlation")
plt.plot(autoRed,"r")

plt.subplot(3,1,2)
plt.title("Green auto correlation")
plt.plot(autoGreen,"g")

plt.subplot(3,1,3)
plt.title("Blue auto correlation")
plt.plot(autoBlue,"b")
plt.show()

# -------------------- Finding peaks ------------------- #

redPeaks = []
peaks_red_temp = sig.find_peaks(autoRed)
for i in range(len(peaks_red_temp)-1):
    for j in peaks_red_temp[i]:
        redPeaks.append(j)

bluePeaks = []
peaks_blue_temp = sig.find_peaks(autoBlue)
for i in range(len(peaks_blue_temp)-1):
    for j in peaks_blue_temp[i]:
        bluePeaks.append(j)

greenPeaks = []
peaks_green_temp = sig.find_peaks(autoGreen)
for i in range(len(peaks_green_temp)-1):
    for j in peaks_green_temp[i]:
        greenPeaks.append(j)

plt.subplot(3,1,1)
xsR = np.linspace(0, len(autoRed), len(autoRed))
plt.title("Red Autocorrelation with peaks")
plt.plot(xsR,autoRed,"-rD",markevery=redPeaks)


plt.subplot(3,1,2)
xsB = np.linspace(0, len(autoBlue), len(autoBlue))
plt.title("Blue Autocorrelation with peaks") 
plt.plot(xsB,autoBlue,"-bD",markevery=bluePeaks)


plt.subplot(3,1,3)
xsG = np.linspace(0, len(autoGreen), len(autoGreen))
plt.title("Green Autocorrelation with peaks")
plt.plot(xsG,autoGreen,"-gD",markevery=greenPeaks)

plt.show()

# -------------------- Moving average filter ------------------- #

