import random
import pandas as pd 
import numpy as np
import math
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

class geometry():

    def __init__(self):
        pass 
    
    def add_material(self,material,radius):
        self.material=material
        self.radius=radius

    def graph(self,colo):
        radius=np.array(self.radius)
        colo=colo
        circle=[]
        for i in range (len(radius)):
            if i==0:
                logic=True
            else:
                logic=False
            circle.append(plt.Circle((0,0),radius[i],color=colo[i],fill=logic))
            plt.gca().add_patch(circle[i])
        plt.axis("scaLed")
       # plt.show()

"""necessary data loading """

u_f_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/U-235(fission).csv")
u_s_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/U-235(scattering).csv")
u_a_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/U-235(absorption).csv")
H_s_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/H-1(scattering).csv")
H_a_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/H-1(absorption).csv")
Be_a_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/Cross section data for berilium_scattering_and absorption.csv")
D_s_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/Cross section data for Deuterium_scattering.csv")
D_a_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/Cross section data for deuterium_ absorption.csv")
O_s_i=pd.read_csv("/home/ibne_walid/Documents/csv data file/Cross section data for oxygen_scattering_and absorption.csv")

#molar mass and the density 
#U_molar_mass=235
# O2_molar_mass= 36
# Be=10 
# H2=2
# D2=4
# 

"""D2O_density=1.1 gm/cm3
BeO2_density=3.02 gm/cm3
H2_density=0.07 g/cm3
UO2_density=10.97 g/cm3"""

Be_s_i=Be_a_i.drop('cross section (a)',axis='columns')
Be_a_i=Be_a_i.drop('cross section (s)',axis='columns')
O_a_i=O_s_i.drop('cross section (s)',axis='columns')
O_s_i=O_s_i.drop('cross section (a)',axis='columns')

#-----------------------------------------------------------------------------------------------------------------------------
#interpolating the cross section data 
N=6.632*10**23
molar_mass=235
density=10.91
atom_density=(N/molar_mass)*density*10**-24


u_f=interp1d((10**-6)*u_f_i['Incident energy'],atom_density*u_f_i['cross_section'],"linear")
u_s=interp1d((10**-6)*u_s_i['Incident energy'],atom_density*u_s_i['cross section'],"cubic")
u_a=interp1d((10**-6)*u_a_i['Incident energy'],atom_density*u_a_i['cross section'],"cubic")

#for berilum
molar_mass=10
density=1.85
atom_density=(N/molar_mass)*density*10**-24

Be_s=interp1d((10**-6)*Be_s_i['Incident energy'],atom_density*Be_s_i['cross section (s)'],"cubic")
Be_a=interp1d((10**-6)*Be_a_i['Incident energy'],atom_density*Be_a_i['cross section (a)'],"cubic")

#for deutorium 
molar_mass=4
density=1.11
atom_density=(N/molar_mass)*density*10**-24

D_s=interp1d((10**-6)*D_s_i['Incident energy'],atom_density*D_s_i['cross section (s)'],"linear")
D_a=interp1d((10**-6)*D_a_i['Incident energy'],atom_density*D_a_i['cross section (a)'],"cubic")

#for oxygen 
molar_mass=36
density=1.429
atom_density=(N/molar_mass)*density*10**-24

O_s=interp1d((10**-6)*O_s_i['Incident energy'],atom_density*O_s_i["cross section (s)"],"cubic")
O_a=interp1d((10**-6)*O_a_i['Incident energy'],atom_density*O_a_i["cross section (a)"],"cubic")

#for hydrogen  
molar_mass=2
density=0.07
atom_density=(N/molar_mass)*density*10**-24

H_s=interp1d((10**-6)*H_s_i['Incident energy'],atom_density*H_s_i["cross section"],"cubic")
H_a=interp1d((10**-6)*H_a_i['Incident energy'],atom_density*H_a_i["cross section"],"cubic")


#---------------------------------------------------------------------------------------------------------------------------
#simulation input part
radius=[1,1.1,1.5,1.7,2,2.1]
material=['u','h2','d20','be02','d2o','ad']
color=['red','g','blue','pink','blue','green']

sim=geometry()
sim.add_material(material,radius)
sim.graph(color)

#------------------------------------------------------------------------------------------------------------------------------------------
def absorbtion_cross_section(geometry,neutron_energy):
	neutron_energy=neutron_energy
	#there will csv cross section data file from where data will be calculated
	if geometry == "U":
	#will call the interpolated function
		return u_a(neutron_energy)
	elif geometry =="H2":
	#will call the interpolated function
		return H_a(neutron_energy)
	elif geometry =="D2O":
	#will call the interpolated function
		return D_a(neutron_energy)+0.5*O_a(neutron_energy)
	elif geometry=="BeO2":
		return Be_a(neutron_energy)+O_a(neutron_energy)
	else:
		return 0
	


def scattering_cross_section(geometry,neutron_energy):
	neutron_energy=neutron_energy
	#there will csv cross section data file from where data will be calculated
	if geometry =="U":
	#will call the interpolated function
		return u_s(neutron_energy)
	elif geometry =="H2":
	#will call the interpolated function
		return H_s(neutron_energy)
	elif geometry =="D2O":
	#will call the interpolated function
		return D_s(neutron_energy)+0.5*O_s(neutron_energy)
	elif geometry=="BeO2":
		return Be_s(neutron_energy)+O_s(neutron_energy)
	else:
		return 0

def fission_cross_section(geometry,neutron_energy):
	neutron_energy=neutron_energy
	if geometry =="U":
		return u_f(neutron_energy)
	else:
		return 0
		

def energy_updater(energy,molar_mass):
	A=molar_mass
	E=energy
	alpha=1-((A-1)/(A+1))**2
	delta_E=np.random.uniform(0,alpha*E)
	
	return E-delta_E
#-------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------

#number_of_neutrons=int(input("How many number of neutrons----"))
#skip=int(input("enter how many gen to skip"))	
skip=60
number_of_neutrons=500
no_gen_sim=200				      
position_matrix=np.zeros((number_of_neutrons,3))
k_eff=np.zeros(no_gen_sim)
energy=[]
new_gen_neutron=np.zeros(no_gen_sim)
for i in range (number_of_neutrons):
	position_matrix[i][0]=np.random.uniform(0,radius[0])                    #radius record 
	position_matrix[i][1]=np.random.uniform(-180,180)               #theta record 
	position_matrix[i][2]=np.random.uniform(-90,90)	  		        #phi record 
	energy.append(np.random.uniform(2,4))
#---------------------------------------------------------------------------------------------------------------------------

print( "number_of_neutron         -------to------      new_gen_neutronare produced---------------   k_eff" )	
for j in range(no_gen_sim):

	#list
	r=[]
	theta=[]
	phi=[]
	energy_new=[]
	
		
	for i in range (number_of_neutrons):
        
        #location copy
		x=position_matrix[i][0]*math.sin(position_matrix[i][2])*math.cos(position_matrix[i][1])
		y=position_matrix[i][0]*math.sin(position_matrix[i][2])*math.sin(position_matrix[i][1])
		z=position_matrix[i][0]*math.cos(position_matrix[i][2])
		Engergy = energy[i]
		alive=True
		
		while alive:
		
		# core 
			if math.sqrt(x**2+y**2+z**2)<radius[0]:
			
			#that means the neutron is inside the core 
				
				sigma_s=scattering_cross_section("U",Engergy)
				sigma_a=absorbtion_cross_section("U",Engergy)
				sigma_f=fission_cross_section("U",Engergy)
				
				total_sigma=sigma_s+sigma_f+sigma_a
				
				reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma])
				
				#need to figure out how to make a bias here ------done
				
				if reaction_type =="scattering":
					
					random_parameter=np.random.rand()
					theta_move=random.uniform(0,360)
					phi_move=random.uniform(0,180)
					
					l= -math.log(1-random_parameter)/total_sigma
					
					x = x+l*math.sin(phi_move)*math.cos(theta_move)
					y = y+l*math.sin(phi_move)*math.sin(theta_move)
					z = z+l*math.cos(phi_move)
					
					Engergy =energy_updater(Engergy,235)
			    		
				elif reaction_type=="fission":
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
					
				
						r.append(math.sqrt(x**2+y**2+z**2))
						theta.append(math.atan(y/x))
						phi.append(math.atan(math.sqrt(x**2+y**2)/z))
						
						energy_new.append(np.random.uniform(9,14))
					
					alive=False 
				else:
					alive=False 
        		
        		#2nd layerelif 
			if math.sqrt(x**2+y**2+z**2)>radius[0] and math.sqrt(x**2+y**2+z**2) <radius[1]:     #need to be fixed 
			
				#that means the neutron is outside of the core and in the 2nd layer  
				#material=['U','H2','D20','Be02','D2o','ad']
				
				sigma_s=scattering_cross_section("H2",Engergy)
				sigma_a=absorbtion_cross_section("H2",Engergy)
				sigma_f=fission_cross_section("H2",Engergy)
					
				total_sigma=sigma_s+sigma_f+sigma_a
				
				reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma])
					
					#need to figure out how to make a bias here----> done  
					
				if reaction_type =="scattering":
					random_parameter=np.random.rand()
					theta_move=random.uniform(0,360)
					phi_move=random.uniform(0,180)
					
					l= -math.log(1-random_parameter)/total_sigma
					
					x = x+l*math.sin(phi_move)*math.cos(theta_move)
					y = y+l*math.sin(phi_move)*math.sin(theta_move)
					z = z+l*math.cos(phi_move)
					Engergy =energy_updater(Engergy,2)
				    	
				elif reaction_type=="fission":
						
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
						
						#location has to be saved for new initiation 
						#there will be a loop to create the same location in a matrix
						#for the same number of neutron 
						
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2))
						theta.append(math.atan(y/x))
						phi.append(math.atan(math.sqrt(x**2+y**2)/z))
						energy_new.append(np.random.unifrom(9,14))
					
						alive=False 
				else:
					alive=False
				#2nd layer 
			elif math.sqrt(x**2+y**2+z**2)>radius[1] and math.sqrt(x**2+y**2+z**2) <radius[2]:   #need to be fixed 
			
				#that means the neutron is inside the D2O layer 
				#material=['U','H2','D20','Be02','D2o']
					
				sigma_s=scattering_cross_section("D2O",Engergy)
				sigma_f=absorbtion_cross_section("D2O",Engergy)
				sigma_f=fission_cross_section("D2O",Engergy)
					
				total_sigma=sigma_s+sigma_f+sigma_a
				
				reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma])
					
					#need to figure out how to make a bias here 
					
				if reaction_type =="scattering":
					
					random_parameter=np.random.rand()
					theta_move=random.uniform(0,360)
					phi_move=random.uniform(0,180)
					
					l= -math.log(1-random_parameter)/total_sigma
					
					x = x+l*math.sin(phi_move)*math.cos(theta_move)
					y = y+l*math.sin(phi_move)*math.sin(theta_move)
					z = z+l*math.cos(phi_move)
					
					Engergy =energy_updater(Engergy,molar_mass=20)
				    	
				elif reaction_type=="fission":
						
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
						
						#location has to be saved for new initiation 
						#there will be a loop to create the same location in a matrix
						#for the same number of neutron 
						
					for k in range(new_neutron):
						
						r.append(math.sqrt(x**2+y**2+z**2))
						theta.append(math.atan(y/x))
						phi.append(math.atan(math.sqrt(x**2+y**2)/z))
							
						energy_new.append(np.random.unifrom(9,14))
																
						alive=False 
				else:
					alive=False 
						
				#3rd layer 
			elif math.sqrt(x**2+y**2+z**2)>radius[2] and math.sqrt(x**2+y**2+z**2) <radius[3]:
			
				#that means the neutron is inside the BeO2
				#material=['U','H2','D20','Be02','D2o'] 
					
				sigma_s=scattering_cross_section("BeO2",Engergy)
				sigma_f=absorbtion_cross_section("BeO2",Engergy)
				sigma_f=fission_cross_section("BeO2",Engergy)
					
				total_sigma=sigma_s+sigma_f+sigma_a
				
				reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma])
					
					#need to figure out how to make a bias here 
					
				if reaction_type =="scattering":
					
					random_parameter=np.random.rand()
					theta_move=random.uniform(0,360)
					phi_move=random.uniform(0,180)
					
					l= -math.log(1-random_parameter)/total_sigma
					
					x = x+l*math.sin(phi_move)*math.cos(theta_move)
					y = y+l*math.sin(phi_move)*math.sin(theta_move)
					z = z+l*math.cos(phi_move)
					
					Engergy =energy_updater(Engergy,molar_mass=46)
				    	
				elif reaction_type=="fission":
				
						
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
						
						#location has to be saved for new initiation 
						#there will be a loop to create the same location in a matrix
						#for the same number of neutron 
						
					for k in range(new_neutron):
						
						r.append(math.sqrt(x**2+y**2+z**2))
						theta.append(math.atan(y/x))
						phi.append(math.atan(math.sqrt(x**2+y**2)/z))
						energy_new.append(np.random.unifrom(9,14))
					
						
						alive=False 
				else:
					alive=False
			#4th layer 
			elif math.sqrt(x**2+y**2+z**2)>radius[3] and math.sqrt(x**2+y**2+z**2) <radius[4]:
			
				#that means the neutron is inside the D2O
				#material=['U','H2','D20','Be02','D2O'] 
				
				sigma_s=scattering_cross_section("D2O",Engergy)
				sigma_f=absorbtion_cross_section('D2O',Engergy)
				sigma_f=fission_cross_section('D2O',Engergy)
					
				total_sigma=sigma_s+sigma_f+sigma_a
				
				reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma])
					
					#need to figure out how to make a bias here 
					
				if reaction_type =="scattering":
					
					random_parameter=np.random.rand()
					theta_move=random.uniform(0,360)
					phi_move=random.uniform(0,180)
					
					l= -math.log(1-random_parameter)/total_sigma
					
					x = x+l*math.sin(phi_move)*math.cos(theta_move)
					y = y+l*math.sin(phi_move)*math.sin(theta_move)
					z = z+l*math.cos(phi_move)
					
					Engergy =energy_updater(Engergy,20)
				    	
				elif reaction_type=="fission":
						
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
						
						#location has to be saved for new initiation 
						#there will be a loop to create the same location in a matrix
						#for the same number of neutron 
						
					for k in range(new_neutron):
							
						r.append(math.sqrt(x**2+y**2+z**2))
						theta.append(math.atan(y/x))
						phi.append(math.atan(math.sqrt(x**2+y**2)/z))
						energy_new.append(np.random.unifrom(9,14))
					
						
						alive=False 
				else:
					alive=False
			else:
				alive=False
		
	position_matrix=np.zeros((len(r),3))
	for k in range(len(r)):

		position_matrix[k][0]=r[k]
		position_matrix[k][1]=theta[k]
		position_matrix[k][2]=phi[k]
	#position_matrix[:][0]=r
	#position_matrix[:][1]=theta
	#position_matrix[:][2]=phi
		
	energy=np.zeros(len(energy_new))
	energy=energy_new
		
		
	k_eff[j]=new_gen_neutron[j]/number_of_neutrons
	print("from------------- ", number_of_neutrons ," -------to------ ",new_gen_neutron[j],"are produced--------------- ",k_eff[j] )
	number_of_neutrons=int(new_gen_neutron[j])
