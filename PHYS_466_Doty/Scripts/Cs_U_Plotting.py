# Patrick McMillin
# PHYS 466 Dr. Doty
# 13 February 2018

import numpy as np
import matplotlib.pyplot as plt

def main():
    Cs_Small = np.loadtxt('Experimental_Data/LG18_Really_Small.txt')
    Cs_Large = np.loadtxt('Experimental_Data/SM18_Really_Large.txt')
    U = np.loadtxt('Experimental_Data/U238.txt')

    # Using Cs-137 as a reference
    # [Theoretical peak (keV), Observed peak (channel num)]
    Peaks = [662., 227.]

    Plotting_Cs_Large(Cs_Large, Peaks)
    Plotting_Cs_Small(Cs_Small, Peaks)
    Plotting_Cs_Together(Cs_Large, Cs_Small, Peaks)
    Plotting_U(U, Peaks)
    Plotting_Cs_U(Cs_Large, U, Peaks)
    
def Plotting_Cs_Small(Cs_Small, Peaks):
    x = range(len(Cs_Small))
    for i in range(len(x)):
        x[i] = x[i] * (Peaks[0] / Peaks[1])
    plt.plot(x, Cs_Small)
    plt.title('Spectrum of Cs-137 in the Small Detector')
    plt.xlabel('keV')
    plt.ylabel('Counts')
    #photopeak
    plt.axvline(x=662, color = 'black', linestyle = 'dashed')
    plt.text(668,2000,'Photopeak', fontsize = 8)
    plt.text(668, 1900, '662 keV')
    #compton edge
    plt.axvline(x=482, color = 'black', linestyle = 'dashed')
    plt.text(488,2000,'Compton Edge')
    plt.text(488, 1900, 'Theory=476 keV', fontsize = 7)
    plt.text(488, 1800, 'Exp=482 keV', fontsize = 7)
    #backscatter peak
    plt.axvline(x=200, color = 'black', linestyle = 'dashed')
    plt.text(206,2000,'Back Scatter Peak')
    plt.text(206,1900,'Theory=185 keV', fontsize = 7)
    plt.text(206,1800,'Exp=200 keV', fontsize = 7)
    #barium x-ray
    plt.axvline(x=38, color = 'black', linestyle = 'dashed')
    plt.text(45,2000,'Barium X-ray')
    plt.text(45,1900,'Theory=42.6 keV', fontsize = 7)
    plt.text(45,1800,'Exp=38 keV', fontsize = 7)
    plt.savefig('Plots/Cs_137_Small.png')
    plt.show()
    plt.clf()
    
def Plotting_Cs_Large(Cs_Large, Peaks):
    x = range(len(Cs_Large))
    for i in range(len(x)):
        x[i] = x[i] * (Peaks[0] / Peaks[1])
    plt.plot(x, Cs_Large)
    plt.title('Spectrum of Cs-137 in the Large Detector')
    plt.xlabel('keV')
    plt.ylabel('Counts')
    #photopeak
    plt.axvline(x=662, color = 'black', linestyle = 'dashed')
    plt.text(668,2400,'Photopeak', fontsize = 8)
    plt.text(668, 2300, '662 keV')
    #compton edge
    plt.axvline(x=477, color = 'black', linestyle = 'dashed')
    plt.text(485,2400,'Compton Edge')
    plt.text(485, 2300, 'Theory=476 keV', fontsize = 7)
    plt.text(485,2200,'Exp=477 keV', fontsize = 7)
    #backscatter peak
    plt.axvline(x=187, color = 'black', linestyle = 'dashed')
    plt.text(200,2400,'Back Scatter Peak')
    plt.text(200,2300,'Theory=185 keV', fontsize = 7)
    plt.text(200,2200,'Exp=187 keV', fontsize = 7)
    #barium x-ray
    plt.axvline(x=21, color = 'black', linestyle = 'dashed')
    plt.text(30,2400,'Barium X-ray')
    plt.text(30,2300,'Theory=42.6 keV', fontsize = 7)
    plt.text(30,2200,'Exp=21 keV', fontsize = 7)
    plt.savefig('Plots/Cs_137_Large.png')
    plt.show()
    plt.clf()

def Plotting_U(U, Peaks):
    x = range(len(U))
    for i in range(len(x)):
        x[i] = x[i] * (Peaks[0] / Peaks[1])
    plt.plot(x, U)
    plt.title('Spectrum of U-238')
    plt.xlabel('keV')
    plt.ylabel('Counts')
    #photopeak
    plt.axvline(x=594, color = 'black', linestyle = 'dashed')
    plt.text(600, 2000, 'Bismouth', fontsize=8)
    plt.text(600, 1900, 'Theory=609 keV', fontsize=8)
    plt.text(600, 1800, 'Exp=594 keV', fontsize=8)
    #lead, theory using nf=1, ni=3 (13.6 eq)
    plt.axvline(x=84, color = 'black', linestyle = 'dashed')
    plt.text(85, 3200, 'Lead')
    plt.text(85, 3100,'Theory=81.3 keV')
    plt.text(85, 3000, 'Exp=84 keV')
    plt.axvline(x=190, color = 'black', linestyle = 'dashed', ymax = 0.90)
    plt.text(195, 2700, 'Radon')
    plt.text(195, 2600, 'Theory=186 keV')
    plt.text(195, 2500, 'Exp=190 keV')
    plt.axvline(x=246, color = 'black', linestyle = 'dashed', ymax = 0.75)
    plt.text(250, 2300, 'Lead')
    plt.text(250, 2200, 'Theory=241 keV')
    plt.text(250, 2100, 'Exp=246 keV')
    plt.axvline(x=297, color = 'black', linestyle = 'dashed', ymax = 0.62)
    plt.text(300, 1900,'Lead')
    plt.text(300, 1800,'Theory=295 keV')
    plt.text(300, 1700,'Exp=297 keV')
    plt.axvline(x=353, color = 'black', linestyle = 'dashed', ymax = 0.48)
    plt.text(358, 1500, 'Lead')
    plt.text(358, 1400, 'Theory=351 keV')
    plt.text(358, 1300, 'Exp=353 keV')
    plt.savefig('Plots/U_238.png')
    plt.show()
    plt.clf()

def Plotting_Cs_Together(Cs_big, Cs_small, Peaks):
    x = range(len(Cs_big))
    for i in range(len(x)):
        x[i] = x[i] * (Peaks[0] / Peaks[1])
    plt.plot(x, Cs_small, label='Small Detector', color='orange')
    plt.plot(x, Cs_big, label='Large Detector', color = 'blue')
    plt.title('Spectrum of Cs-137 in the Small and Large Detectors')
    plt.axvline(x=662, color = 'black', linestyle = 'dashed')
    plt.axvline(x=482, linestyle = 'dashed', color = 'orange')
    plt.axvline(x=200, linestyle = 'dashed', color = 'orange')
    plt.axvline(x=38, linestyle = 'dashed', color = 'orange')
    plt.axvline(x=477, color = 'blue', linestyle = 'dashed')
    plt.axvline(x=187, color = 'blue', linestyle = 'dashed')
    plt.axvline(x=21, color = 'blue', linestyle = 'dashed')
    plt.xlabel('keV')
    plt.ylabel('Counts')
    plt.legend()
    plt.savefig('Plots/Cs_Together.png')
    plt.show()
        
def Plotting_Cs_U(Cs_big, U, Peaks):
    x = range(len(Cs_big))
    for i in range(len(x)):
        x[i] = x[i] * (Peaks[0] / Peaks[1])
    plt.plot(x, Cs_big, label='Cs-137')
    plt.plot(x, U, label='U-238')
    plt.title('Spectrum of Cs-137 and U-238')
    plt.xlabel('keV')
    plt.ylabel('Counts')
    plt.legend()
    plt.savefig('Plots/Cs_U_Together.png')
    plt.show()
    
main()
