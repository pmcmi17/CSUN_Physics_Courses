import numpy as np
import pprint as pp
import matplotlib.pyplot as plt

def main():
    # Get and restructure data into a dictionary. 
    File = open('Data/Easyspin_Fitting_Best_Vals_Without_20_45.txt')
    Data_Unsplit = File.read()
    Data_Strings = Data_Unsplit.split('\n')
    Data_List = []
    Data_Dict = {}
    for i in range(len(Data_Strings)-1):
        Temp_List = Data_Strings[i].split(',')
        for j in range(len(Temp_List)):
            Temp_List[j] = float(Temp_List[j])
        Data_List.append(Temp_List)
    for i in range(len(Data_List)):
        Data_Dict[str(Data_List[i][0])] = [Data_List[i][1],
                                           Data_List[i][2:]]
    Data = Calc_Iso_and_RDiff(Data_Dict)
    Plotting(Data)
    # {'Temp':RMSD,[g_xx,g_yy,g_zz,A_xx,A_yy,A_zz,<bleh>,<bleh2>,logdiff],g_iso,A_iso}
    #pp.pprint(Data_Dict)
    
def Calc_Iso_and_RDiff(Data):
    for key in Data:
        Data[key].append(sum(Data[key][1][0:3])/3)
        Data[key].append(sum(Data[key][1][3:6])/3)
        Data[key].append(10**(-1*Data[key][1][8])*(10**9)/6)
    return Data

def Plotting(Data):
    # Plots A_iso vs T, g_iso vs T, and Rot_Diff vs T.
    A_iso_Point_List = []
    g_iso_Point_List = []
    Rot_Diff_Point_List = []
    for key in Data:
        g_iso_Point_List.append([float(key),Data[key][2]])
        A_iso_Point_List.append([float(key),Data[key][3]])
        Rot_Diff_Point_List.append([float(key),Data[key][4]])
    plt.figure(1)
    A_iso = []
    T_A_iso = []
    for i in range(len(A_iso_Point_List)):
        plt.scatter(A_iso_Point_List[i][0]+273.15,A_iso_Point_List[i][1])
        A_iso.append(A_iso_Point_List[i][1])
        T_A_iso.append(A_iso_Point_List[i][0]+273.15)
    plt.title(r'A$_{isometric}$ vs Temperature ($K$)')
    plt.ylabel(r'A$_{iso}$ ($MHz$)')
    plt.xlabel(r'Temperature ($K$)')
    plt.savefig('Plots/A_iso_plot.pdf')
    plt.show()
    plt.figure(2)
    g_iso = []
    T_g_iso = []
    for i in range(len(g_iso_Point_List)):
        plt.scatter(g_iso_Point_List[i][0]+273.15,g_iso_Point_List[i][1])
        g_iso.append(g_iso_Point_List[i][1])
        T_g_iso.append(g_iso_Point_List[i][0]+273.15)
    plt.title(r'g$_{isometric}$ vs Temperature ($K$)')
    plt.ylabel(r'g$_{iso}$ ($test$)')
    plt.xlabel(r'Temperature ($K$)')
    plt.savefig('Plots/g_iso_plot.pdf')
    plt.show()
    plt.figure(3)
    tau = []
    T_tau = []
    for i in range(len(Rot_Diff_Point_List)):
        plt.scatter(Rot_Diff_Point_List[i][0]+273.15,Rot_Diff_Point_List[i][1])
        tau.append(Rot_Diff_Point_List[i][1])
        T_tau.append(Rot_Diff_Point_List[i][0]+273.15)
    plt.title(r'Rotational Diffusion ($ns$) vs Temperature ($K$)')
    plt.ylabel(r'$\tau$ ($ns$)')
    plt.xlabel(r'Temperature ($K$)')
    plt.savefig('Plots/Rot_Dif_plot.pdf')
    plt.show()
    
main()
