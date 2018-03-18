import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy as sp

Raw_Data = [23, 48, 24, 19, 4, 2]

Average = 0
for i in range(len(Raw_Data)):
    Average += (i * Raw_Data[i])
Average = Average / float(sum(Raw_Data))

Std = np.sqrt(Average)

Norm_Fact = sum(Raw_Data)
Average_opt = 1.46738148

poisson = lambda r: Norm_Fact * np.exp(-Average_opt) * (Average_opt ** r) / float(sp.special.factorial(r))

Raw_Theo = []
Raw_Partial_Chi = []
for i in range(len(Raw_Data)):
    Raw_Theo.append(poisson(i))
    Raw_Partial_Chi.append(((Raw_Theo[i] - Raw_Data[i]) ** 2) / Raw_Theo[i])
Raw_Chi_Squared = sum(Raw_Partial_Chi)

print(Raw_Data)
print(Raw_Theo)
print(Raw_Partial_Chi)
print(Raw_Chi_Squared)

Raw_x = range(len(Raw_Data))
plt.scatter(Raw_x, Raw_Data, color = 'red', label = 'Collected Data')
plt.scatter(Raw_x, Raw_Theo, color = 'blue', label = 'Fitted Poisson Function', marker = 's')
plt.xlim(-0.5, 5.5)
plt.title('Distribution of Counts in LO 1100')
plt.xlabel('Counts')
plt.text(4.2, 55, 'McMillin, Patrick')
plt.text(3, 40, r'$\mu = $' + str(round(Average, 2)))
plt.text(3, 37, r'$\sigma = $' + str(round(Std, 2)))
plt.text(3, 34, r'$\chi^2 = $' + str(round(Raw_Chi_Squared, 2)))
plt.text(3, 31, r'$DoF = 6 - 2 = 4$')
plt.text(3, 28, r'$\chi^2_r = $' + str(round(Raw_Chi_Squared / 4, 2)))
plt.text(3, 25, 'Accept the fit (23% - 31%)')
plt.legend()
plt.savefig('Plots/Raw_Poisson.pdf')
plt.show()

New_Data_Bin = Raw_Data[4] + Raw_Data[5]
Significant_Data = Raw_Data
del(Significant_Data[5])
del(Significant_Data[4])
Significant_Data.append(New_Data_Bin)

New_Theo_Val = Raw_Theo[4] + Raw_Theo[5]
Significant_Theo = Raw_Theo
del(Significant_Theo[5])
del(Significant_Theo[4])
Significant_Theo.append(New_Theo_Val)

New_Partial_Chi_Val = Raw_Partial_Chi[4] + Raw_Partial_Chi[5]
Significant_Partial_Chi = Raw_Partial_Chi
del(Raw_Partial_Chi[5])
del(Raw_Partial_Chi[4])
Significant_Partial_Chi.append(New_Partial_Chi_Val)

Significant_Chi_Squared = sum(Significant_Partial_Chi)

print(Significant_Data)
print(Significant_Theo)
print(Significant_Partial_Chi)
print(Significant_Chi_Squared)

plt.clf()

Significant_x = range(len(Significant_Data))
plt.scatter(Significant_x, Significant_Data, color = 'red', label = 'Collected Data')
plt.scatter(Significant_x, Significant_Theo, color = 'blue', label = 'Fitted Poisson Function', marker = 's')
plt.xlim(-0.5, 5.5)
plt.title('Distribution of Counts in LO 1100')
plt.xlabel('Counts')
plt.text(4.2, 55, 'McMillin, Patrick')
plt.text(3, 40, r'$\mu = $' + str(round(Average, 2)))
plt.text(3, 37, r'$\sigma = $' + str(round(Std, 2)))
plt.text(3, 34, r'$\chi^2 = $' + str(round(Raw_Chi_Squared, 2)))
plt.text(3, 31, r'$DoF = 5 - 2 = 3$')
plt.text(3, 28, r'$\chi^2_r = $' + str(round(Raw_Chi_Squared / 3, 2)))
plt.text(3, 25, 'Accept the fit (14% - 19%)')
plt.legend()
plt.savefig('Plots/Significant_Poisson.pdf')
plt.show()
    
