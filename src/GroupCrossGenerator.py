import pandas as pd
import numpy as np

p_a=pd.read_csv('/home/shochcho/Documents/Thermal_hydraulics_and_neutronics_coupling-main/cross section data/U-235 absorption.csv')

y=np.array(p_a['Cross section'])
x=np.array(p_a['Incident energy'])

Group_num=600
h=int(len(y)/Group_num)
Gcross=np.zeros(len(y))
s=np.arange(0,len(x),step=h)
v=np.zeros(len(s)-1)
m=np.zeros(len(s)-1)

for i in range(len(s)-1):
    v[i]=np.std(y[s[i]:s[i+1]])
    m[i]=np.mean(y[s[i]:s[i+1]])
    Gcross[s[i]:s[i+1]]=m[i]

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.plot(x,Gcross,color='red')
plt.yscale('log')
plt.xscale('log')
plt.ylabel("Cross section (barn )")
plt.xlabel("energy (eV)")
plt.legend(["Cross Section","Grouped Cross section"])
