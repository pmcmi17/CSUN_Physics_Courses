# Patrick McMillin
# PHYS 466  Dr. Doty
# 20 February 2018

import numpy as np
import matplotlib.pyplot as plt

def main():
    Data = np.loadtxt('Experimental_Data/Quarter_300.txt')
    Events = Bin_Events(Data)
    #print(Events)
    print("Mean of raw data:")
    print(np.mean(Data))
    print("Standard Deviation of Data:")
    print(np.std(Data))
    print("Mean of # in a row:")
    print(np.mean(Events))
    print("Standard Deviation of # in a row:")
    print(np.std(Events))

    
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
    # Binned all but the last one so add it manually
    Events.append(1)
    return Events

def line(x):
    return (1./2.)**x

def Plotting(Events):
    n, bins, trash = plt.hist(Events)
    print(n)
    #print(bins)
    x = np.linspace(1,10,1000)
    plt.plot(x,160*line(x))
    plt.savefig('Plots/Coin_Flip_Histo.pdf')
    plt.show()
    
main()
