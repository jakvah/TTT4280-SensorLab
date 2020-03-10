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

plt.subplot(3,1,1)
plt.title("Red time signal")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(red,"r")

plt.subplot(3,1,2)
plt.title("Green time signal")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(green,"g")

plt.subplot(3,1,3)
plt.title("Blue time signal")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(blue,"b")
plt.show()

# -------------------- FFT ------------------- #

fft_red = np.fft.rfft(red,axis = 0)
fft_green = np.fft.rfft(green,axis = 0)
fft_blue = np.fft.rfft(blue,axis = 0)

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

auto_red_temp = np.correlate(red,red,"full")
auto_green_temp = np.correlate(green,green,"full")
auto_blue_temp = np.correlate(blue,blue,"full")

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
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(autoRed,"r")

plt.subplot(3,1,2)
plt.title("Green auto correlation")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(autoGreen,"g")

plt.subplot(3,1,3)
plt.title("Blue auto correlation")
plt.xlabel("Sample")
plt.ylabel("Value")
plt.plot(autoBlue,"b")
plt.show()



goldenOldies = bml.findpeak(nyauto[int(len(nyauto)/2):])
print(goldenOldies)
print("lengden er:",len(goldenOldies))

for j in range(len(goldenOldies)):
    if j == 0 or j == len(goldenOldies):
        continue
    else:
        prev_index = goldenOldies[j-1]
        curr_index = goldenOldies[j]
        diff = curr_index - prev_index
        print("Diff mellom peakpair nr",    j-1,":")
        print(diff)

