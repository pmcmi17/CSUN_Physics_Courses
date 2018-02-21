#import numpy as np
import pprint as pp
import matplotlib.pyplot as plt

def main():
    # Get and restructure data into a dictionary. 
    File = open('Data/Easyspin_Fitting_Best_Vals.txt')
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
    # {'Temp':RMSD,[g_xx,g_yy,g_zz,A_xx,A_yy,A_zz, <SOMETHING>],g_iso,A_iso}
    # The identity of the last three numbers in the parameter list are not known.
    #pp.pprint(Data_Dict)
    
def Calc_Iso_and_RDiff(Data):
    for key in Data:
        Data[key].append(sum(Data[key][1][0:3])/3)
        Data[key].append(sum(Data[key][1][3:6])/3)
        # If we knew which parameter corresponded to the logDiff, here
        # is where we would calculate it. For now, I have made the calculation,
        # just need to know the index of the number. It's placeholder value is 'j'.
        #Data_Dict[key].append(10**(Data_Dict[key][i][j])*(10**9)/6)
    return Data

def Plotting(Data):
    # Plots A_iso vs T, g_iso vs T, and Rot_Diff vs T.
    A_iso_Point_List = []
    g_iso_Point_List = []
    #Rot_Diff_Point_List = []
    for key in Data:
        g_iso_Point_List.append([float(key),Data[key][2]])
        A_iso_Point_List.append([float(key),Data[key][3]])
        #Rot_Diff_Point_List.append([float(key),Data[key][4]])
    #print(A_iso_Point_List)
    #print(g_iso_Point_List)
    #print(Rot_Diff_Point_List)
    plt.figure(1)
    for i in range(len(A_iso_Point_List)):
        plt.scatter(A_iso_Point_List[i][0],A_iso_Point_List[i][1])
    plt.show()
    plt.figure(2)
    for i in range(len(g_iso_Point_List)):
        plt.scatter(g_iso_Point_List[i][0],g_iso_Point_List[i][1])
    plt.show()
    '''
    plt.figure(3)
    for i in range(len(Rot_Diff_Point_List)):
        plt.scatter(Rot_Diff_Point_List[i][0],Rot_Diff_Point_List[i][1])
    plt.show()
    '''
    
main()
