import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# List index is the number of counts.
# List value is the number of instances of the
# count number being observed.

Binned_Data = [23, 48, 24, 19, 4, 2]
# Initial guesses for the Poisson fitting
x0 = []

# chi-squared function to minimize
def chi_squared(x0):
    # Defines the poisson function
    poisson = lambda x: x
    T = []
    chi_sq = []
    for i in range(len(Binned_Data)):
        T_i = poisson(i)
        T.append(T_i)
        chi_sq.append((T_i-Binned_Data[i])**2/T_i)
    Chi_Squared = sum(chi_sq)
    return Chi_Squared
# Calls the minimizer
#Min = opt.minimize(chi_squared,x0)
# gets the minimized values
#x_opt = Min.x

# Plots the fitted function and the experimental data. 
plt.figure(1)
x = np.linspace(-0.5,5.5,1000)
# Defines the poisson function to plot.
#poisson = lambda x: x
plt.scatter(range(len(Binned_Data)),Binned_Data,
         color= 'red', label='Collected Data')
#plt.plot(x,poisson(x), color='blue',label='Fitted Function')
plt.xlim(-0.5, 5.5)
plt.title('Poisson Data')
plt.xlabel('Counts')
plt.legend()
plt.show()
