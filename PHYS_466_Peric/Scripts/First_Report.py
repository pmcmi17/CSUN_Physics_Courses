import numpy as np
import pprint as pp
import scipy.optimize as opt
import matplotlib.pyplot as plt

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
# Calculates the isometric values for A and g, and the rotdif.
for key in Data_Dict:
    Data_Dict[key].append(sum(Data_Dict[key][1][0:3])/3)
    Data_Dict[key].append(sum(Data_Dict[key][1][3:6])/3)
    Data_Dict[key].append(10**(-1*Data_Dict[key][1][8])*(10**9)/6)
# {'Temp':RMSD,[g_xx,g_yy,g_zz,A_xx,A_yy,A_zz,<bleh>,<bleh2>,logdiff],g_iso,A_iso}
#pp.pprint(Data_Dict)

A_iso_Point_List = []
g_iso_Point_List = []
Rot_Diff_Point_List = []
for key in Data_Dict:
    g_iso_Point_List.append([float(key),Data_Dict[key][2]])
    A_iso_Point_List.append([float(key),Data_Dict[key][3]])
    Rot_Diff_Point_List.append([float(key),Data_Dict[key][4]])
A_iso = []
T_A_iso = []
for i in range(len(A_iso_Point_List)):
    A_iso.append(A_iso_Point_List[i][1])
    T_A_iso.append(A_iso_Point_List[i][0]+273.15)
g_iso = []
T_g_iso = []
for i in range(len(g_iso_Point_List)):
    g_iso.append(g_iso_Point_List[i][1])
    T_g_iso.append(g_iso_Point_List[i][0]+273.15)
tau = []
T_tau = []
for i in range(len(Rot_Diff_Point_List)):
    tau.append(Rot_Diff_Point_List[i][1])
    T_tau.append(Rot_Diff_Point_List[i][0]+273.15)
    
x0_line_g = [0.00001, 2] #[m, b]
x0_line_A = [0.001, 41] #[m, b]
x0_arrhenius = [0.00000006, 250, -7000] #[tau_0, T_0, EA]

def chi_sq_line_g(x0):
    line = lambda x: ((x0[0] * x) + x0[1])
    Theo = []
    chi_sq = []
    for i in range(len(g_iso)):
        Theo_i = line(T_g_iso[i])
        Theo.append(Theo_i)
        chi_sq.append((Theo_i-g_iso[i])**2/Theo_i)
    Chi_Squared = sum(chi_sq)
    return Chi_Squared

def chi_sq_line_A(x0):
    line = lambda x: ((x0[0] * x) + x0[1])
    Theo = []
    chi_sq = []
    for i in range(len(A_iso)):
        Theo_i = line(T_A_iso[i])
        Theo.append(Theo_i)
        chi_sq.append((Theo_i-A_iso[i])**2/Theo_i)
    Chi_Squared = sum(chi_sq)
    return Chi_Squared

def chi_sq_arrhenius(x0):
    R = 8.314
    arrhenius = lambda x: (x0[0]*np.exp(-x0[2]/((x-x0[1])*R)))
    Theo = []
    chi_sq = []
    for i in range(len(tau)):
        Theo_i = arrhenius(T_tau[i])
        Theo.append(Theo_i)
        chi_sq.append((Theo_i-tau[i])**2/Theo_i)
    Chi_Squared = sum(chi_sq)
    return Chi_Squared

# Line fitting for the g factor
result_line_g = opt.minimize(chi_sq_line_g, x0_line_g)
# Line fitting for the hyper-fine interaction
result_line_A = opt.minimize(chi_sq_line_A, x0_line_A)
# Line fitting for an arrhenius function for rotational diffusion
result_arrhenius = opt.minimize(chi_sq_arrhenius, x0_arrhenius)

def line(x,x_opt):
    return (x_opt[0]*x)+x_opt[1]

def arrhenius(x,x_opt):
    R = 8.314
    return (x_opt[0]*np.exp(-x_opt[2]/(R*(x-x_opt[1]))))

x = np.linspace(295,380,1000)

print(result_line_g.x)
print(result_line_A.x)
print(result_arrhenius.x)

plt.figure(1)
for i in range(len(A_iso_Point_List)):
    plt.scatter(A_iso_Point_List[i][0]+273.15,A_iso_Point_List[i][1], color = 'red')
plt.plot(x,line(x,result_line_A.x))
plt.title(r'A$_{isometric}$ vs Temperature ($K$)')
plt.ylabel(r'A$_{iso}$ ($MHz$)')
plt.xlabel(r'Temperature ($K$)')
plt.savefig('Plots/A_iso_plot.pdf')
plt.show()
plt.figure(2)
for i in range(len(g_iso_Point_List)):
    plt.scatter(g_iso_Point_List[i][0]+273.15,g_iso_Point_List[i][1], color = 'red')
plt.plot(x,line(x,result_line_g.x))
plt.title(r'g$_{isometric}$ vs Temperature ($K$)')
plt.ylabel(r'g$_{iso}$ ($dimensionless$)')
plt.xlabel(r'Temperature ($K$)')
plt.savefig('Plots/g_iso_plot.pdf')
plt.show()
plt.figure(3)
for i in range(len(Rot_Diff_Point_List)):
    plt.scatter(Rot_Diff_Point_List[i][0]+273.15,Rot_Diff_Point_List[i][1], color = 'red')
plt.plot(x,arrhenius(x,result_arrhenius.x))
plt.title(r'Rotational Diffusion ($ns$) vs Temperature ($K$)')
plt.ylabel(r'$\tau$ ($ns$)')
plt.xlabel(r'Temperature ($K$)')
plt.savefig('Plots/Rot_Dif_plot.pdf')
plt.show()
