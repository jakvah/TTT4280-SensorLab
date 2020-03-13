# Bugges matteland
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import scipy.signal as sig

def findPeaks(data):
    redPeaks = []
    peaks_red_temp = sig.find_peaks(data)
    for i in range(len(peaks_red_temp)-1):
        for j in peaks_red_temp[i]:
            redPeaks.append(j)
    return redPeaks

# Returnes average index distance from each peak.
def findAvgPeakDistance(peakIndexes):
    sum = 0
    for i in range(len(peakIndexes)-1):
        currIndex = peakIndexes[i]
        nextIndex = peakIndexes[i+1]
        diff = nextIndex - currIndex
        sum += diff

    avg = sum / (len(peakIndexes) -1)
    return avg



def movingAverage(dataSet,Window):
    cumsum, moving_aves = [0], []

    for i, x in enumerate(dataSet, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=Window:
            moving_ave = (cumsum[i] - cumsum[i-Window])/Window
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    return moving_aves

def findpeak(data):    
    maxValue = max(data)
    maxIndex = data.index(maxValue)

    peakLocations = [maxIndex]
    minLocations = []
    # Help variables to find local min and max.
    currLocalMax = maxValue
    currLocalMin = maxValue 
    lookingForMin = True
"""
    for i in range(maxIndex+1,len(data)):
        if lookingForMin:
            currVal = data[i]
            prevVal = data[-1]
            if currVal < prevVal:
                currLocalMin = currVal
            if currVal > prevVal and prevVal == currLocalMin:
                minLocations.append(i-1)
        

            try:
                prevVal = data[i-1]
                currVal = data[i]
                nextVal = data[i+1]
                if currVal > prevVal and currVal > nextVal:
                    peakLocations.append(i) 
            except IndexError as e:
                if i == 0:
                    currVal = data[i]
                    nextVal = data[i+1]
                    if currVal > prevVal:
                        peakLocations.append(i)
                else:
                    prevVal = data[i-1]
                    currVal = data[i]
                    if currVal > prevVal:
                        peakLocations.append(i)
                    
    return peakLocations
    """

def determineX(x_12,x_13,x_23, n_12, n_13,n_23, f_s,a):
    c = 3*10**8

    x_21 = x_12
    x_31 = x_13
    x_32 = x_23

    t_12 = n_12/f_s
    t_13 = n_13/f_s
    t_23 = n_23/f_s

    t_21 = t_12
    t_31 = t_13
    t_32 = t_23   

    #sum = (x_12*t_12 + x_13*t_13 + x_21*t_21 + x_23*t_23 + x_31*t_31 + x_32*t_32)
    #x = ((2*c) / (9*a**2))*sum

    x = (-(np.sqrt(3)*a/3)*t_12)+((np.sqrt(3)*a/3)*t_13)+(np.sqrt(3)*a*t_23)
    return x

def calculateAngle(n_21,n_31,n_32):    
    arg = (np.sqrt(3)*(n_21 + n_32)) / (n_21 - n_31 - 2*n_32)
    
    angle = np.arctan(arg)

    return angle

def makeAnglePositive(ang):
    if ang < 0:
        ang = 360 + ang
    return ang

def circlePlot(angle):
    N = 360
    bottom = 0
    max_height = 4

    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = max_height*np.random.rand(N)
    width = ((2*np.pi) / N) + 0.01

    for i in range(N):
        radii[i] = 0
        if i == int(round(angle)):
            radii[i] = (max_height*1)

    ax = plt.subplot(111, polar=True)
    bars = ax.bar(theta, radii, width=width, bottom=bottom)
    ax.set_yticklabels([])
    ax.set_title("Plot av vinkelen: " + str(int(round(angle))) + " i grader:")

    # Spicy farger
    for r, bar in zip(radii, bars): 
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.8)

    plt.show()


def removeDC(seq):
    sum_seq = 0
    for sample in seq:
        sum_seq += sample   

    mean_seq = sum_seq / len(seq)

    seq_mod = []


    for sample in seq:
        new = sample - mean_seq
        seq_mod.append(new)

    return seq_mod