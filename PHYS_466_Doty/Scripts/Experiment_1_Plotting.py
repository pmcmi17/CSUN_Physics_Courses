# Patrick McMillin
# PHYS 466 Dr. Doty
# 30 January 2018 - Heatmap Plot
# 6 February 2018 - Histogram and Gaussian

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import pprint as pp
from Integrate_Gaussian import Integrate_Trapezoid

def main():
    Data = Load_Data()
    Mean, Std_Dev = Get_Mean_and_Std_Deviation(Data)
    #Plot_Heat_Map(Data, Mean, Std_Dev)
    #Plot_Histogram_and_Gaussian(Data, Mean, Std_Dev)
    Plot_Five_Bin_Hist_and_Chi_Fit(Data)
    
def Load_Data():
    Data = np.loadtxt('Experimental_Data/Experiment_1_Data.txt')
    return Data

def Reshape_Data(Data):
    # Reshapes the 240 by 1 array into a 16 by 15 array (most square configuration).
    # With more or less data, this will be unusable.
    # Consider making a function that finds the two closest integer factors.
    Data = np.reshape(np.asarray(Data), (16, 15))
    return Data

def Plot_Heat_Map(Data, Mean, Std):
    Data = Reshape_Data(Data)
    Plot, axis = plt.subplots()
    Heatmap = axis.pcolor(Data, cmap = plt.cm.Oranges)
    plt.colorbar(Heatmap)
    plt.title('Experiment 1 Data Heat Map')
    plt.xlabel('Mean=' + Mean + ', Standard Deviation=' + Std)
    Plot.savefig('Plots/Experiment_1_Heat_Map.pdf')
    #plt.show()
    
def Get_Mean_and_Std_Deviation(Data):
    # Round to significant digits
    Mean = str(round(np.mean(Data), 1))
    Std = str(round(np.std(Data), 1))
    return Mean, Std

def Plot_Histogram_and_Gaussian(Data, Mean, Std_Dev):
    # 'bin' argument to 'plt.hist' must be an integer
    Number_of_Bins = int(max(Data) - min(Data))
    Hist = plt.hist(Data, bins = Number_of_Bins, label = 'Collected Data')
    # vertical lines for sigma values
    plt.axvline(x = (float(Mean) + float(Std_Dev)), ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.axvline(x = (float(Mean) - float(Std_Dev)), ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.axvline(x = (float(Mean) + (2 * float(Std_Dev))), ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.axvline(x = (float(Mean) - (2 * float(Std_Dev))), ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    # plot gaussian by eye
    x = np.linspace(min(Data), max(Data), num = 1000)
    Sigma = 12.5
    Center = 84.5
    Fudge_Factor = 16.5
    Gaussian_by_eye = Fudge_Factor*np.exp((-1 / 2)*(((x - Center) / (Sigma)) ** 2))
    plt.plot(x, Gaussian_by_eye, label = 'Gaussian (By Eye)')

    # Plots gaussian by the data
    Real_Gauss = False
    if Real_Gauss == True:
        Std = float(Std_Dev)
        Mu = float(Mean)
        Counts = Counter(Data)
        Norm_Factor = max(Counts.values())
        Gaussian_by_data = Norm_Factor*np.exp((-1 / 2)*(((x - Mu) / (Std)) ** 2))
        plt.plot(x, Gaussian_by_data, label = 'Gaussian (By Data)', color = 'red')
        plt.text(104.5, 9, 'Normalization ', color = 'red')
        plt.text(104.5, 8, 'Factor = ' + str(Norm_Factor), color = 'red')
        plt.text(104.5, 7, r'$\mu$ = ' + str(Mu), color = 'red')
        plt.text(104.5, 6, r'$\sigma$ = ' + str(Std), color = 'red')

    # cosmetics
    plt.title('Distribution of Radiation in LO 1100')
    plt.xlabel('Counts per Measurement')
    plt.text(55, 16, r'$\mu$ = ' + str(Mean) + r'$\pm$' + str(0.5))
    plt.text(53.45, 15, r'$\sqrt{\mu}$ = ' + str(round(np.sqrt(float(Mean)), 1)))
    plt.text(55, 14, r'$\sigma$ = ' + str(Std_Dev))
    plt.text(55, 13, 'Fudge Factor = ' + str(Fudge_Factor), color = 'orange')
    plt.text(55, 12, 'X = ' + str(Center), color = 'orange')
    plt.text(55, 11, r'$\sigma$ = ' + str(Sigma), color = 'orange')
    plt.text(110, 19, 'McMillin, Patrick')
    plt.text(67, 10.5, '-2' + r'$\sigma$')
    plt.text(76.45, 10.5, '-1' + r'$\sigma$')
    plt.text(95, 10.5, '+1' + r'$\sigma$')
    plt.text(104, 10.5, '+2' + r'$\sigma$')
    plt.legend()
    
    plt.savefig('Plots/Experiment_1_Histogram_and_Gaussian.pdf')
    plt.show()

def Gaussian_Function(x, mu = 85.4, sigma = 9.3, norm = 240.):
    return (norm/(sigma*np.sqrt(2*(np.pi))))*np.exp(-1*((x-mu)**2)/(2*(sigma**2)))
    
def Plot_Five_Bin_Hist_and_Chi_Fit(Data):
    Mean = round(np.mean(Data), 1)
    Std = round(np.std(Data), 1)
    #Normalization_Factor = 2700
    x = np.linspace(min(Data), max(Data), 1000)
    Num_Bins = 5
    Bin_Width = (max(Data) - min(Data)) / float(Num_Bins)
    Center_Points = [[],[]]
    Bins = {}
    for i in range(Num_Bins):
        Bounds = [(min(Data) + (i * Bin_Width)),
                  (min(Data) + ((i + 1) * Bin_Width))]
        Bounds_Sigma_Space = [(Bounds[0] - Mean) / Std,
                              (Bounds[1] - Mean) / Std]
        Bins[i+1] = [Bounds, [], Bounds_Sigma_Space]
    for i in range(len(Data)):
        for j in range(len(Bins)):
            if Bins[j+1][0][0] <= Data[i] < Bins[j+1][0][1]:
                Bins[j+1][1].append(Data[i])
                break
            if Data[i] == max(Data):
                Bins[5][1].append(Data[i])
                break
    bounds_printable = []
    for i in range(Num_Bins):
        Center_Points[0].append(Bins[i+1][0][0] + (Bin_Width / 2))
        Center_Points[1].append(len(Bins[i+1][1]))
        bounds_printable.append(Bins[i+1][0])
        
    Chi_Squared = 0.
    T = []
    E = []
    Part_Chi = []
    for i in range(Num_Bins):
        T_i = Integrate_Trapezoid(Gaussian_Function,
                                  Bins[i+1][0][0],
                                  Bins[i+1][0][1], 0.001)
        T.append(round(T_i,1))
        E_i = float(len(Bins[i+1][1]))
        E.append(round(E_i,1))
        Part_Chi_Squared = ((T_i-E_i)**2)/(T_i)
        Part_Chi.append(round(Part_Chi_Squared,1))
        Chi_Squared += Part_Chi_Squared
    plt.hist(Data, Num_Bins, label = 'Experimental Data')
    plt.plot(x, (Bin_Width * Gaussian_Function(x)), label = 'Gaussian')
    plt.scatter(Center_Points[0], Center_Points[1],
                color = 'black', label = 'Bin Centers')
    plt.axvline(x = (float(Mean)), #ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.axvline(x = (float(Mean) + float(Std)), ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.axvline(x = (float(Mean) - float(Std)), #ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.axvline(x = (float(Mean) + (2 * float(Std))), ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.axvline(x = (float(Mean) - (2 * float(Std))), #ymax = 0.748,
                color = 'black', linestyle = 'dashed')
    plt.title('Distribution of Raditation in LO 1100')
    plt.xlabel('Counts')
    plt.text(54, 120, r'$\mu$ = '+str(Mean)+r'$\pm$'+str(round(Std/np.sqrt(len(Data)),1)))
    plt.text(54, 115, r'$\sigma$ = '+str(Std))
    plt.text(54, 110, r'$\chi^{2}$ = '+str(round(Chi_Squared,1)))
    plt.text(54, 105, r'$\chi^{2}_{r}$ = '+str(round(Chi_Squared/2,1)))
    plt.text(54, 100, r'Prob($\chi^{2} \geq \chi^{2}_{r}$)')
    plt.text(54, 95, str(18)+'% at 3 DoF')
    plt.text(54, 80, r'$\sigma_m = \frac{\sigma}{\sqrt{N}}$')
    plt.text(100, 140, 'McMillin, Patrick')
    plt.legend()
    plt.savefig('Plots/Experiment_1_Five_Bin_Chi_Fit.pdf')
    plt.show()
    
main()

