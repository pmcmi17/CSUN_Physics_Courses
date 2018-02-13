# McMillin, Patrick
# PHYS 466 Dr. Doty
# 6 February 2018

import numpy as np
import matplotlib.pyplot as plt

def main():
    Berzerk = True
    Voltage, Counts = Load_and_Separate(Berzerk)
    Plot(Voltage, Counts, Berzerk)
    
def Load_and_Separate(Berzerk):
    Data = np.loadtxt('Experimental_Data/Experiment_2_Data.txt')
    #loadtxt loads as one array, so we need to split it up
    Voltage = []
    Counts = []
    for i in range(len(Data)):
        Counts.append(Data[i][1])
        if Berzerk == True:
            Voltage.append(Data[i][0]*(662./7.75))
        else:
            Voltage.append(Data[i][0])
    return Voltage, Counts

def Plot(Voltage, Counts, Berzerk):
    plt.plot(Voltage, Counts, label = 'Collected Data')
    plt.title('X-Ray Spectrum of Cs-137')
    plt.ylabel('Counts')
    error_V = 0.01
    error_KeV = error_V * 662
    Theory_x_ray = round(((13.6 * ((56) ** 2) * ((1/(1**2))-(1/(2**2))))/1000), 1)
    if Berzerk == True:
        plt.xlim([0, 900])
        plt.xlabel('keV')
        plt.axvline(x = (65.0), linestyle = 'dashed', color = 'orange',
                    label = 'Ba X-Ray', ymin = .28)
        plt.text(70, 90, 'Ba X-Ray', fontsize = 7)
        plt.text(70, 85, r'0.75$\pm$' + str(error_V) + ' V', fontsize = 5)
        plt.text(70, 80, r'65.0$\pm$' + str(error_KeV) + ' keV', fontsize = 5)
        plt.text(70, 75, 'Theory: ' + str(Theory_x_ray) + ' keV', fontsize = 4)
        plt.axvline(x = 662, linestyle = 'dashed', color = 'red', label = 'Photopeak')
        plt.text(664, 90, 'Photopeak', fontsize = 10)
        plt.text(664, 85, r'(7.75$\pm$' + str(error_V) + ' V)', fontsize = 8)
        plt.text(664, 80, r'(662$\pm$' + str(error_KeV) + ' keV)', fontsize = 8)
        plt.axvline(x = 473, linestyle = 'dashed', color = 'green',
                    label = 'Compton Edge')
        plt.text(475, 90, 'Compton Edge', fontsize = 9)
        plt.text(475, 85, r'(5.50$\pm$' + str(error_V) + ' V)', fontsize = 7)
        plt.text(475, 80, r'(473$\pm$' + str(error_KeV) + ' keV)', fontsize = 7)
        plt.text(475, 75, r'Theory $E_e$ = 476 keV', fontsize = 6)
        plt.axvline(x = 172, linestyle = 'dashed', color = 'black', ymin = .28,
                    label = 'Back Scatter Peak')
        plt.text(175, 90, 'Back Scatter Peak', fontsize = 10)
        plt.text(175, 85, r'(2.00$\pm$' + str(error_V) + ' V)', fontsize = 8)
        plt.text(175, 80, r'(172$\pm$' + str(error_KeV) + ' keV)', fontsize = 8)
        plt.text(175, 75, 'Theory E\' = 185 keV', fontsize = 8)
        x = np.linspace(500, 800, 1000)
        Sigma = 50.5
        Center = 662
        Fudge_Factor = 76.5
        Gaussian = Fudge_Factor*np.exp((-1 / 2)*(((x - Center) / (Sigma)) ** 2))
        FWHM = round((2 * np.sqrt(2*np.log(2)) * Sigma), 0)
        plt.text(720, 40, 'Center = ' + str(Center) + ' keV', fontsize = 7,
                 color = 'red')
        plt.text(720, 35, 'Std = ' + str(Sigma) + ' keV', fontsize = 7, color = 'red')
        plt.text(720, 30, 'Fudge Factor = ' + str(Fudge_Factor), fontsize = 7,
                 color = 'red')
        plt.plot(x, Gaussian, label = 'Gaussian (By Eye)', color = 'red')
        plt.axhline(y = (Fudge_Factor / 2), xmin = 0.69, xmax = 0.78,
                    color = 'red')
        plt.text(700, 60, 'FWHM', fontsize = 8, color = 'red')
        plt.text(700, 55, '(' + str(FWHM) + ' keV)', fontsize = 8, color = 'red')
    else:
        plt.xlim([0,10.5])
        plt.xlabel('V')
        plt.axvline(x = 7.75, linestyle = 'dashed', color = 'red')
        plt.text(7.8, 90, 'Photopeak (7.8 V)')
        plt.text(7.8, 85, '(662 KeV)')
        plt.axvline(x = 4.97, linestyle = 'dashed', color = 'red')
        plt.text(5, 90, 'Compton Edge')
        plt.text(5, 85, '(4.9 V)')
        plt.text(5, 80, '(431 KeV)')
        plt.axvline(x = 2, linestyle = 'dashed', color = 'red')
        plt.text(2.1, 90, 'Back Scatter')
        plt.text(2.1, 85, 'Peak (2.0 V)')
        plt.text(2.1, 80, '(172 KeV)')
    plt.ylim([0, 100])
    plt.legend(loc = 3, prop={'size': 8})
    plt.text(700, 110, 'McMillin, Patrick')
    plt.text(700, 106, 'PHYS 466  Dr. Doty')
    plt.text(700, 102, '6 February 2018')
    plt.savefig('Plots/Experiment_2_Spectrum.png')
    plt.show()
    
main()
