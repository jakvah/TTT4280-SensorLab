# Jakob Vahlin, SPRING 2020

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import buggesmatteland as bml

WINDOW_SIZE = 10
FRAMERATE = 40

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

# -------------------- Moving average filter ------------------- #

redMvAvg = bml.movingAverage(red,WINDOW_SIZE)
blueMvAvg = bml.movingAverage(blue,WINDOW_SIZE)
greenMvAvg = bml.movingAverage(green,WINDOW_SIZE)

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
plt.plot(fft_red,"r")

plt.subplot(3,1,2)
plt.title("Green FFT")
plt.plot(fft_green,"g")

plt.subplot(3,1,3)
plt.title("Blue FFT")
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

redPeaks = bml.findPeaks(autoRed)
bluePeaks = bml.findPeaks(autoBlue)
greenPeaks = bml.findPeaks(autoGreen)

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

# -------------------- Computing pulse ------------------- #

avgPeakRed = bml.findAvgPeakDistance(redPeaks)
avgPeakBlue = bml.findAvgPeakDistance(bluePeaks)
print()
print("-------------------- PULSE CALCULATIONS -------------------- ")
print()
print("Average red sample peak diff is: ", avgPeakRed)
print("At",FRAMERATE,"fps that is a pulse of: ", avgPeakRed / FRAMERATE, " Hz, or ", (avgPeakRed / FRAMERATE) * 60, " beats pr minute!" )
print("-------------------------------------------------------------")
print("Average blue sample peak diff is: ", avgPeakBlue)
print("At",FRAMERATE,"fps that is a pulse of: ", avgPeakBlue / FRAMERATE, " Hz, or ", (avgPeakBlue / FRAMERATE) * 60, " beats pr minute!" )



