# Bugges matteland
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci


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

    sum = (x_12*t_12 + x_13*t_13 + x_21*t_21 + x_23*t_23 + x_31*t_31 + x_32*t_32)
    x = ((2*c) / (9*a**2))*sum

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

    # Spicy farger
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.8)

    plt.show()

