import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

def findpeak(pikk):
    peaks = []
    dikk = {}
    for i in range(len(pikk)):
        if i == 0 or i == len(pikk):
            continue
        else:
            try:
                prevVal = pikk[i-1]
                currVal = pikk[i]
                nextVal = pikk[i+1]
                if currVal > prevVal and currVal > nextVal:
                    peaks.append(i) 
            except IndexError as e:
                prevVal = pikk[i-1]
                currVal = pikk[i]
                if currVal > prevVal:
                    peaks.append(i)
                    
    return peaks


godStuff = np.loadtxt("film5.txt")
godStuff = sig.detrend(godStuff,axis = 0)
red = godStuff[:,0]


"""
red = []
for l in godStuff:
    red.append(l[0])
"""
print("goodstuff")
print(godStuff.shape)

print("Data fra txt")
print(godStuff)

fft_red = np.fft.rfft(red,axis = 0)
print("data fra fft")
print(fft_red)

plt.plot(red)
plt.show()
plt.plot(np.abs(fft_red))
plt.show()

print()

print("autocorr my ballz")
autocorr = np.correlate(fft_red,fft_red,"full")
autocorr_tits = np.correlate(red,red,"full")

print(len(autocorr))

nyauto = []
for j in autocorr:
    nyauto.append(j)

nyauto_2 = []
for j in autocorr_tits:
    nyauto_2.append(j)



plt.plot(nyauto)
plt.show(nyauto)

plt.plot(nyauto_2)
plt.show()



goldenOldies = findpeak(nyauto[int(len(nyauto)/2):])
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

