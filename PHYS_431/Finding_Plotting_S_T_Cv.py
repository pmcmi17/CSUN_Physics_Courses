'''
Uses unrestricted partitions to find physical variables and plots.
Patrick McMillin
PHYS 431, Dr. Taheri
Last modified: 5 December 2017
'''
'''
Section 3.3 outlines the 'centered-difference' procedure. T = dU/dS
for the ith value of T: T[i] = (U[i+1]-U[i-1]) / (S[i+1]-S[i-1])
Similarly, we can generate Cv in a loop by calculating Cv = dU/dT
Cv[i] = (U[i+1]-U[i-1]) / (T[i+1]-T[i-1])
'''

import numpy as np
import matplotlib.pyplot as plt
# Script written to find the partitions
import Unrestricted_Partitions
# Calls function to generate partitions and assigns them to a list.
Partitions = Unrestricted_Partitions.Generate_Unrestricted_Partitions()
# Energy levels are just the numerical values we found the
# unrestricted partitions for (i.e. the numbers 0 through 100).
# For simplicity, $\eta$ = k = 1.
Energy = range(0,101)
Entropy = []
# Takes the logarithm of all microstates to find S/k.
for i in Partitions:
    Entropy.append(np.log(i))
Temperature = [0]
Heat_Capacity = [0]
# Temperatures
for i in range(1,(len(Energy)-1)): # NOTE: len()-1 since we will not have a Energy[101]
    Temperature.append((Energy[i+1]-Energy[i-1]) / (Entropy[i+1]-Entropy[i-1]))
# Heat capacities
for i in range(1,(len(Energy)-2)): # NOTE: len()-1 since we will not have a Temperature[100]
    Heat_Capacity.append((Energy[i+1]-Energy[i-1]) / (Temperature[i+1]-Temperature[i-1]))
del Temperature[0]
plt.figure(1)
plt.scatter(Temperature, Heat_Capacity)
plt.title('Heat Capacity (C/k) vs Temperature (kT/$\eta$)')
plt.xlabel('Temperature (kT/$\eta$)')
plt.ylabel('Heat Capacity (C/k)')
plt.savefig('T_vs_Cv.pdf')

plt.figure(2)
Temp_List = np.linspace(1,9,100)
Ramanujan_Heat_Capacity_Coefficient = ((np.pi)**2)/3
P = plt.scatter(Temperature, Heat_Capacity)
R = plt.plot(Temp_List, (Ramanujan_Heat_Capacity_Coefficient*Temp_List)-2, 'r-')
plt.title('Ramanujans Approximation for Heat Capacity (C/k) vs Temperature (kT/$\eta$)')
plt.xlabel('Temperature (kT/$\eta$)')
plt.ylabel('Heat Capacity (C/k)')
plt.legend(['Heat capacity from Ramanujan approximation','Heat capacity from unrestricted partitions'])
plt.savefig('Ramanujan_T_vs_Cv.pdf')

print("Ramanujan approximation for q=10:", Ramanujan_Approximation[10])
print("Actual value for q=10:", Partitions[10])
print("Ramanujan approximation for q=100:", Ramanujan_Approximation[100])
print("Actual value for q=100:", Partitions[100])
Ramanujan_Approximation = [1]
for i in range(1,len(Energy)):
    Ramanujan_Approximation.append((np.exp(np.pi*np.sqrt(2*i/3)))/(4*np.sqrt(3)*i))
