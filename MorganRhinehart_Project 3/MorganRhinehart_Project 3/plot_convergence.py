#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np


n_step = 2001
T_lst, Pot_E_lst, Pressure_lst = [], [], []
T_col_ind, Pot_E_col_ind, Pressure_col_ind = 1, 3, 4
all_lines = open('log_NVT__Deform_1000K.lammps','r').readlines()

for line_ind, line in enumerate(all_lines):
    if 'Step          Temp' in line:
        for val_line in all_lines[line_ind+1:line_ind+n_step+1]:
            val_strs = val_line.split('  ')
            count = 0
            for i, item in enumerate(val_strs):
                try:
                    item_val = eval(item)
                    count += 1
                except:
                    continue
                if count-1 == T_col_ind:
                    T_lst.append(item_val)
                elif count-1 == Pot_E_col_ind:
                    Pot_E_lst.append(item_val)
                elif count-1 == Pressure_col_ind:
                    Pressure_lst.append(item_val)
        break

T_arry, Pot_E_arry, Pressure_arry = np.array(T_lst), \
        np.array(Pot_E_lst), np.array(Pressure_lst)

timeSteps = range(len(T_arry))

fig = plt.figure(figsize=(4,6))
plt.subplot(3,1,1)
plt.plot(timeSteps,T_arry,'-k')
plt.ylabel('Temperature (K)',fontsize=15)
plt.subplot(3,1,2)
plt.plot(timeSteps,Pot_E_arry,'-k')
plt.ylabel('E$_{total}$ (eV)',fontsize=15)
plt.subplot(3,1,3)
plt.plot(timeSteps,Pressure_arry,'-k')
plt.ylabel('Pressure (bar)',fontsize=15)

plt.tight_layout()
plt.savefig('convergence.pdf')


