import numpy as np
import matplotlib.pyplot as plt
from Integrate_Gaussian import Integrate_Trapezoid
import scipy.optimize as opt

Data = np.loadtxt('Experimental_Data/Experiment_1_Data.txt')
Num_Bins = 5
n, bins, trash = plt.hist(Data, Num_Bins, label = 'Experimental Data')
# initial guesses
x0 = [85.9, 9.6, 240]
#def gauss(x, norm=norm, sig=sig, mean=mean):
#    return (norm/(sig*np.sqrt(2*(np.pi))))*np.exp(-1*((x-mean)**2)/(2*(sig**2)))
def chi_sq(x0):
    gauss = lambda x: (x0[2]/(x0[1]*np.sqrt(2*(np.pi))))*np.exp(-1*((x-x0[0])**2)/(2*(x0[1]**2)))
    T = []
    chi_sq = []
    for i in range(len(bins)-1):
        T_i = Integrate_Trapezoid(gauss, bins[i], bins[i+1], 0.001)
        T.append(T_i)
        chi_sq.append((T_i-n[i])**2/T_i)
    Chi_Squared = sum(chi_sq)
    return Chi_Squared

#result = opt.minimize(chi_sq,x0)
#x_opt = result.x
#print(x_opt)
x_opt = [86.03476904, 9.53245969, 241.60610734]

def chi_sq_done(x_opt):
    gauss = lambda x: (x_opt[2]/(x_opt[1]*np.sqrt(2*(np.pi))))*np.exp(-1*((x-x_opt[0])**2)/(2*(x_opt[1]**2)))
    T = []
    chi_sq = []
    for i in range(len(bins)-1):
        T_i = Integrate_Trapezoid(gauss, bins[i], bins[i+1], 0.001)
        T.append(T_i)
        chi_sq.append((T_i-n[i])**2/T_i)
    Chi_Squared = sum(chi_sq)
    return T, chi_sq, Chi_Squared

T, partial_chis, Chi_sq = chi_sq_done(x_opt)
for i in range(len(T)):
    partial_chis[i] = round(partial_chis[i],1)
    T[i] = round(T[i],1)
Chi_sq = round(Chi_sq,1)
print(n)
print(T)
print(partial_chis)
print(Chi_sq)
gauss = lambda x: (x_opt[2]/(x_opt[1]*np.sqrt(2*(np.pi))))*np.exp(-1*((x-x_opt[0])**2)/(2*(x_opt[1]**2)))
x = np.linspace(min(Data), max(Data), 1000)
plt.plot(x, 12*gauss(x), label = 'Fitted Gaussian')
plt.axvline(x = (float(x_opt[0])), #ymax = 0.748,
            color = 'black', linestyle = 'dashed')
plt.axvline(x = (float(x_opt[0]) + float(x_opt[1])), ymax = 0.748,
            color = 'black', linestyle = 'dashed')
plt.axvline(x = (float(x_opt[0]) - float(x_opt[1])), #ymax = 0.748,
            color = 'black', linestyle = 'dashed')
plt.axvline(x = (float(x_opt[0]) + (2 * float(x_opt[1]))), ymax = 0.748,
            color = 'black', linestyle = 'dashed')
plt.axvline(x = (float(x_opt[0]) - (2 * float(x_opt[1]))), #ymax = 0.748,
            color = 'black', linestyle = 'dashed')
plt.title('Distribution of Raditation in LO 1100')
plt.xlabel('Counts')
plt.text(54, 120, r'$\mu$ = '+str(round(x_opt[0],1)))
plt.text(54, 115, r'$\sigma$ = '+str(round(x_opt[1],1)))
plt.text(54, 110,'FF = '+str(round(x_opt[2],1)))
plt.text(54, 105, r'$\chi^{2}$ = '+str(round(Chi_sq,1)))
plt.text(54, 100, r'$\chi^{2}_{r}$ = '+str(round(Chi_sq/2,1)))
plt.text(54, 95, r'Prob($\chi^{2} \geq \chi^{2}_{r}$)')
plt.text(54, 90, str(37)+'% at 2 DoF')
plt.legend()
plt.savefig('Plots/Experiment_1_Chi_Minimization.pdf')

plt.show()
