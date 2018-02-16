# Patrick McMillin
# PHYS 466  Dr. Doty
# 20 February 2018

import numpy as np
import matplotlib.pyplot as plt

def main():
    Data = np.loadtxt('Experimental_Data/Quarter_300.txt')
    Events = Bin_Events(Data)
    #print(Events)
    Plotting(Events)
    
def Bin_Events(Data):
    i = 0
    j = 1
    Events = []
    while i < (len(Data)-1):
        if Data[i] == Data[i+1]:
            j += 1
        else:
            Events.append(j)
            j = 1
        i += 1
    # Binned al but the last one so add it manually
    Events.append(1)
    return Events

def Plotting(Events):
    plt.hist(Events)
    x = np.linspace(1,10,100)
    #plt.plot(x, (80*((1/2)**x)))
    plt.show()
    
main()
