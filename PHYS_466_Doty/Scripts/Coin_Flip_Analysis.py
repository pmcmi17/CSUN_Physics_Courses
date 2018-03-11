# Patrick McMillin
# PHYS 466  Dr. Doty
# 27 February 2018

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from Integrate_Gaussian import Integrate_Trapezoid

def chi_sq_integral(N):
    half_to_x = lambda x: N*(1./2.)**x
    chi_sq = []
    T_i_List = []
    for i in range(len(Bins)-1):
        T_i = Integrate_Trapezoid(half_to_x, Bins[i], Bins[i+1], 0.001)
        #print(Bins[i])
        #print(Bins[i+1])
        T_i_List.append(T_i)
        chi_sq.append((T_i-n[i])**2/T_i)
    Chi_Squared = sum(chi_sq)
    return Chi_Squared

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

def chi_sq_get_T_i_integral(N):
    half_to_x = lambda x: N*(1./2.)**x
    chi_sq = []
    T_i_List = []
    for i in range(len(Bins)-1):
        T_i = Integrate_Trapezoid(half_to_x, Bins[i], Bins[i+1], 0.001)
        T_i_List.append(T_i)
        chi_sq.append((T_i-n[i])**2/T_i)
    Chi_Squared = sum(chi_sq)
    return T_i_List,chi_sq

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

def moment_1(x):
    return (x)*line(x)
def moment_2(x, c=2.08136839802):
    return ((x-c)**2)*line(x)
    
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
    # This is specific to the data! If things change
    # you have to write it better ;)
    Events.append(1)
    return Events

def line(x):
    return (1./2.)**x

def Plotting(Events,N,chisq, moments):
    #Bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10]
    #n = plt.hist(Events, bins=Bins, range=(0,10),
                 #label = 'Experimental Data',
                 #color = 'green')
    #n = n[0]
    #print(N)
    #x = np.linspace(0.5,10.5,1000)
    #plt.plot(x,(N*line(x)), label = 'Theory', color = 'red')
    plt.clf()
    plt.scatter(pts,n,color='blue',label='exp')
    theory=[]
    for i in range(len(pts)):
        theory.append(N*line(pts[i]))
    plt.scatter(pts,theory, color='red', label='Theroy')
    plt.xlim(0.5,10.5)
    plt.ylim(0,100)
    plt.xlabel('Number of heads or tails in a row')
    plt.ylabel('Counts')
    plt.title('Distribution of 300 Coin Flips')
    plt.text(6.4,80, r'$\mu_{Exp}$ = ' + str(round(np.mean(Events),1)))
    plt.text(6.4,75,r'$\sigma_{Exp}$ = ' + str(round(np.std(Events),1)))
    plt.text(6.4,70, r'$\mu_{Th}$ = ' + str(round(moments[0],1)))
    plt.text(6.4,65,r'$\sigma_{Th}$ = ' + str(round(np.sqrt(moments[1]),1)))
    plt.text(6.4,60,'N = ' + str(round(N,2)))
    plt.text(6.4,55,r'$\chi^2$ = ' + str(round(chisq,2)))
    #plt.text(6.4,50,'DoF = 7 - 1 = 6')
    #plt.text(6.4,45,r'$\chi^2_{r}$ = ' + str(round(chisq/6.,2)))
    #plt.text(6.4,40,'Accept the fit: 88-73%')
    plt.text(3, 80, r'$\mu_{Th} = \int_{0}^{100}x(\frac{1}{2})^xdx$')
    plt.text(2.5, 70, r'$\sigma_{Th}^2 = \int_{0}^{100}(x-\mu_{Th})^2(\frac{1}{2})^xdx$')
    plt.text(7.75,110,'McMillin, Patrick')
    plt.legend()
    plt.savefig('Plots/Coin_Flip_Histo.pdf')
    plt.show()
    
Data = np.loadtxt('Experimental_Data/Quarter_300.txt')
Events = Bin_Events(Data)
full = True
if full == True:
    Bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
    pts = [1,2,3,4,5,6,7,8,9,10]
    n = plt.hist(Events, bins=Bins, range=(0,10))
    n = n[0]
    print(n)
else:
    Bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 10.5]
    pts = [1,2,3,4,5,8]
    n = plt.hist(Events, bins=Bins, range=(0,10))
    n = n[0]
    print(n)
N = 154
result_int = opt.minimize(chi_sq_integral,N)
result_points = opt.minimize(chi_sq_points,N)
x_opt_int = result_int.x
x_opt_pts = result_points.x
T_i_List_integral,Partial_Chi_List_integral = chi_sq_get_T_i_integral(float(x_opt_int))
T_i_List_points,Partial_Chi_List_points = chi_sq_get_T_i_points(float(x_opt_pts))

moments = [Integrate_Trapezoid(moment_1, 0, 100, 0.001),
           Integrate_Trapezoid(moment_2, 0, 100, 0.001)]

points = True

if points == True:
    print(T_i_List_points)
    print(Partial_Chi_List_points)
    if full == True:
        print(sum(Partial_Chi_List_points[5:]))
    Plotting(Events,x_opt_pts,result_points.fun, moments)
else:
    #print(T_i_List_integral)
    #print(Partial_Chi_List_integral)
    Plotting(Events,x_opt_int,result_int.fun, moments)
