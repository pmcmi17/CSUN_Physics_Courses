import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from Integrate_Gaussian import Integrate_Trapezoid

def chi_sq_points(N):
    half_to_x = lambda x: N*(1./2.)**x
    chi_sq = []
    T_i_List = []
    for i in range(len(Bins)-1):
        if full == False:
            if Bins[i] == 5.5:
                #Need to ask!
                #Might be 8.
                #thats why this is here.
                T_i = half_to_x(8)
            else:
                T_i = half_to_x(i+1)
            T_i_List.append(T_i)
            chi_sq.append((T_i-n[i])**2/T_i)
        else:
            T_i = half_to_x(i+1)
            T_i_List.append(T_i)
            chi_sq.append((T_i-n[i])**2/T_i)
    Chi_Squared = sum(chi_sq)
    return Chi_Squared

def chi_sq_get_T_i_points(N):
    half_to_x = lambda x: N*(1./2.)**x
    chi_sq = []
    T_i_List = []
    for i in range(len(Bins)-1):
        T_i = half_to_x(i+1)
        T_i_List.append(T_i)
        chi_sq.append((T_i-n[i])**2/T_i)
    Chi_Squared = sum(chi_sq)
    return T_i_List,chi_sq

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
    Events.append(1)
    return Events

def line(x):
    return (1./2.)**x

def Plotting(Events):
    plt.clf()
    pts = range(9)
    del pts[0]
    Theory = []
    for i in pts:
        Theory.append(line(i))
    plt.hist(Events, bins=Bins, range=(0.5,9.5))
    
    
    
Data = np.loadtxt('Experimental_Data/FA_Coins.txt')
Events = Bin_Events(Data)
Bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
n = plt.hist(Events, bins=Bins, range=(0.5,9.5))
n = n[0]
print(n)

Plotting(Events)
