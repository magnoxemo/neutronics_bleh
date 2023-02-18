import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d

data=pd.read_csv("/home/walid_ahammed/Downloads/U-235 fission.csv")


x=np.array(1.6*10**-19*data['Incident energy'])
y=np.array(10**-24*data['cross section'])

cross_section=interp1d(x,y)


T_1=0
T_2=500



#constants 
k=1.38*10**-23 
mass_projectile=1.61*10**-27
mass_target=(235*10**-3)/(6.63*10**23)
A=mass_target/mass_projectile
target_speed=np.sqrt(k*T_2/mass_target)

alpha=A/(k*(T_2-T_1))

def projectile_speed(energy):
    return np.sqrt(2*energy/mass_projectile)

E_relative=np.array((projectile_speed(x)-target_speed)**2*0.5*mass_projectile)
E_r=[]
E=[]
c=[]

"""resonance region spliting """
for i in E_relative:
    if 10**-20<i and i<10**-13:
        E_r.append(i)

        c.append(cross_section(i))       
for i in x:
    if 10**-20<i and i<10**-13:
        E.append(i)
        
E=np.array(E[:len(E_r)])

intergral=0.5*((alpha/(np.pi*E))**0.5)*np.trapz(cross_section(E_r),E_r,dx=0.01)
gamma=np.exp(-alpha*(np.sqrt(E)-np.sqrt(np.array(((projectile_speed(E)-target_speed)**2)*0.5*mass_target)))**2)-np.exp(-alpha*(np.sqrt(E)+np.sqrt(np.array(((projectile_speed(E)-target_speed)**2)*0.5*mass_target)))**2)

output=intergral*gamma/E

plt.figure(figsize=(10,6))
plt.plot(E_r,c,color='green')
plt.scatter(E,c,color='red',marker='.')
plt.plot(E,output,color='black')

plt.xscale("log")
plt.yscale("log")   
plt.xlabel("incident energy")
plt.ylabel("cross section")
plt.legend(["cross section for relative energy ","cross section for given energy ","output"])


"""this code isn't full. something is wrong in the calculation. I need more time to fix it """
