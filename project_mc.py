import random
import pandas as pd 
import numpy as np
import math

"""
this is the first attempt to write a monte carlo code for a spherical nuclear reactor.In this attempt i will not be keeping tracks of the energy distribution.
this code will solve the eigenvalues which will be computed using the formula 

					keff=(number of neutrons in i+1 gen)/ ( number of neutrons in i th gen)  
					
#######################################################################################################################################################################
copy right :

Ibne Walid Ahammed 
Dept of Nuclear Engineering 
University of Dhaka 
		 
"""

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
        plt.show()


radius=[1,1.1,1.5,1.7,2,2.1]
material=['u','h2','d20','be02','d2o','ad']
color=['red','g','blue','pink','blue','green']

sim=geometry()
sim.add_material(material,r)
sim.graph(color)


"""necessary function """

def scatting_cross_section(geometry,neutron_energy=None): 

	#there will csv cross section data file from where data will be calculated 
	if geometry =="core":
		return sigma_s_core
	elif geometry =="water"
		return sigma_s_water
	elif geometry =="reflector":
		return sigma_s_reflector 

def absorbtion_cross_section(geometry,neutron_energy=None):

	#there will csv cross section data file from where data will be calculated
	if geometry =="core":
	#will call the interpolated function
		return sigma_a_core
	elif geometry =="water":
	#will call the interpolated function
		return sigma_a_water
	elif geometry =="reflector":
	#will call the interpolated function
		return sigma_a_reflector
	
def fission_cross_section(geometry,neutron_energy=None):

	#there will csv cross section data file from where data will be calculated
	if geometry =="core":
	#will call the interpolated function 
	
		return sigma_f_core
		
	elif geometry =="water":
	#will call the interpolated function
		return sigma_f_water
		
	elif geometry =="reflector":
	#will call the interpolated function
		return sigma_f_reflector 

def macroscopic_cross_section_data(data_file,density):

    data_file=data_file
    data_file['cross section']=density* data_file["cross section"]
    
    return data_file

def material_composition():

	pass 
	
def energy_updater(Energy):

    del_E=np.random.uniform(0,(1-alpha)*Engergy)
    Engergy=Engergy-del_E
    return Engergy
								
								"""necessary data loading """

u_f=pd.read_csv("/home/ibne_walid/Documents/csv data file/U-235(fission).csv")
u_s=pd.read_csv("/home/ibne_walid/Documents/csv data file/U-235(scattering).csv")
u_a=pd.read_csv("/home/ibne_walid/Documents/csv data file/U-235(absorption).csv")
H_s=pd.read_csv("/home/ibne_walid/Documents/csv data file/H-1(scattering).csv")
H_a=pd.read_csv("/home/ibne_walid/Documents/csv data file/H-1(absorption).csv")
Be_a=pd.read_csv("/home/ibne_walid/Documents/csv data file/Cross section data for berilium_scattering_and absorption.csv")
D_s=pd.read_csv("/home/ibne_walid/Documents/csv data file/Cross section data for Deuterium_scattering.csv")
O_s=pd.read_csv("/home/ibne_walid/Documents/csv data file/Cross section data for oxygen_scattering_and absorption.csv")



sigma_total=sigma_a+sigma_f+sigma_s 
inv_sigma_total=1/sigma_total
							      """initial position distribution"""
							      
position_matrix=np.zeros((number_of_neutrons,3))

for i in range (number_of_neutrons_):
	position_matrix[i][0]=np.random.uniform(0,r)                      #radius record 
	position_matrix[i][1]=np.random.uniform(-np.pi,np.pi)             #theta record 
	position_matrix[i][2]=np.random.uniform(-np.pi/2,np.pi/2)	  #phi record 
	
	
for j in range(no_gen_sim):
	
	new_gen_neutron_no=np.zeros(no_gen_sim)
	
	for i in range (number_of_neutrons):
	        
	        Engergy= #something 
	        
		#location copy
		x=position_matrix[i][0]*math.sin(phi)*math.cos(position_matrix[i][1])
		y=position_matrix[i][0]*math.sin(position_matrix[i][2])*math.sin(position_matrix[i][1])
		z=position_matrix[i][0]*math.cos(position_matrix[i][2])
		
		while alive:
		
		# core 
			if math.sqrt(x**2+y**2+z**2)<radius_core:
			
			#that means the neutron is inside the core 
				
				sigma_s=scattering_cross_section("core",Energy=Engergy)
				sigma_f=absorbtion_cross_section("core",Energy=Engergy)
				sigma_f=fission_cross_section("core",Energy=Engergy)
				
				total_sigma=sigma_s+sigma_f+sigma_a
				
				reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma)
				
				#need to figure out how to make a bias here 
				
				if reaction_type =="scattering":
				
					l= -math.log(1-random parameter)/(scatting_cross_section("scattering")+scatting_cross_section("scattering")	+scatting_cross_section("scattering"))

					theta=random.uniform(0,360)
					phi=random.uniform(0,180)
					x=x+l*math.sin(phi)*math.cos(theta)
			    		y=y+l*math.sin(phi)*math.sin(theta)
			    		z=z+l*math.cos(phi)

			    		x=x+dx
			    		y=y+dy
			    		z=z+dz
			    		
			    		Engergy =energy_updater(Energy)
			    		
				elif reaction_type="fission":
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2)
						theta.append("""i have to write the formula """)
						phi.append("""i have to write the formula """)
						
					
					alive=False 
				else:
					alive=False 
        		
        		#2nd layer 
        			 
        		if math.sqrt(x**2+y**2+z**2)>radius_core and math.sqrt(x**2+y**2+z**2) <radius_clad:
			
			#that means the neutron is outside of the core and in the 2nd layer  
				
			sigma_s=scattering_cross_section("clad",Energy=Engergy)
			sigma_f=absorbtion_cross_section("clad",Energy=Engergy)
			sigma_f=fission_cross_section("clad",Energy=Engergy)
				
			total_sigma=sigma_s+sigma_f+sigma_a
			
			reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma)
				
				#need to figure out how to make a bias here----> done  
				
			if reaction_type =="scattering":
				
				l= -math.log(1-random parameter)/(scatting_cross_section("scattering")+scatting_cross_section("scattering")	+scatting_cross_section("scattering"))

				theta=random.uniform(0,360)
				phi=random.uniform(0,180)
				x=x+l*math.sin(phi)*math.cos(theta)
		    		y=y+l*math.sin(phi)*math.sin(theta)
		    		z=z+l*math.cos(phi)

			    	x=x+dx
			    	y=y+dy
			    	z=z+dz
			    	
			    	Engergy =energy_updater(Energy)
			    	
				elif reaction_type="fission":
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron=new_gen_neutron+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2)
						theta.append("""i have to write the formula """)
						phi.append("""i have to write the formula """)
						
					
					alive=False 
				else:
					alive=False
			#2nd layer 
        			 
        		if math.sqrt(x**2+y**2+z**2)>radius_clad and math.sqrt(x**2+y**2+z**2) <radius_clad2:
			
			#that means the neutron is inside the core 
				
			sigma_s=scattering_cross_section("clad2",Energy=Engergy)
			sigma_f=absorbtion_cross_section("clad2",Energy=Engergy)
			sigma_f=fission_cross_section("clad2",Energy=Engergy)
				
			total_sigma=sigma_s+sigma_f+sigma_a
			
			reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma)
				
				#need to figure out how to make a bias here 
				
			if reaction_type =="scattering":
				
				l= -math.log(1-random parameter)/(scatting_cross_section("scattering")+scatting_cross_section("scattering")	+scatting_cross_section("scattering"))

				theta=random.uniform(0,360)
				phi=random.uniform(0,180)
				x=x+l*math.sin(phi)*math.cos(theta)
		    		y=y+l*math.sin(phi)*math.sin(theta)
		    		z=z+l*math.cos(phi)

			    	x=x+dx
			    	y=y+dy
			    	z=z+dz
			    	
			    	Engergy =energy_updater(Energy)
			    	
				elif reaction_type="fission":
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2)
						theta.append("""i have to write the formula """)
						phi.append("""i have to write the formula """)
						
					
					alive=False 
				else:
					alive=False 
					
			#3rd layer 
        			 
        		if math.sqrt(x**2+y**2+z**2)>radius_clad and math.sqrt(x**2+y**2+z**2) <radius_clad2:
			
			#that means the neutron is inside the core 
				
			sigma_s=scattering_cross_section("core",Energy=Engergy)
			sigma_f=absorbtion_cross_section("core",Energy=Engergy)
			sigma_f=fission_cross_section("core",Energy=Engergy)
				
			total_sigma=sigma_s+sigma_f+sigma_a
			
			reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma)
				
				#need to figure out how to make a bias here 
				
			if reaction_type =="scattering":
				
				l= -math.log(1-random parameter)/(scatting_cross_section("scattering")+scatting_cross_section("scattering")+scatting_cross_section("scattering"))

				theta=random.uniform(0,360)
				phi=random.uniform(0,180)
				x=x+l*math.sin(phi)*math.cos(theta)
		    		y=y+l*math.sin(phi)*math.sin(theta)
		    		z=z+l*math.cos(phi)

			    	x=x+dx
			    	y=y+dy
			    	z=z+dz
			    	
			    	Engergy =energy_updater(Energy)
			    	
			elif reaction_type="fission":
			
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2)
						theta.append("""i have to write the formula """)
						phi.append("""i have to write the formula """)
						
					
					alive=False 
			else:
					alive=False
			#4th layer 
        			 
        		if math.sqrt(x**2+y**2+z**2)>radius_clad and math.sqrt(x**2+y**2+z**2) <radius_clad2:
			
			#that means the neutron is inside the core 
				
			sigma_s=scattering_cross_section("core",Energy=Engergy)
			sigma_f=absorbtion_cross_section("core",Energy=Engergy)
			sigma_f=fission_cross_section("core",Energy=Engergy)
				
			total_sigma=sigma_s+sigma_f+sigma_a
			
			reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma)
				
				#need to figure out how to make a bias here 
				
			if reaction_type =="scattering":
				
				l= -math.log(1-random parameter)/(scatting_cross_section("scattering")+scatting_cross_section("scattering")	+scatting_cross_section("scattering"))

				theta=random.uniform(0,360)
				phi=random.uniform(0,180)
				x=x+l*math.sin(phi)*math.cos(theta)
		    		y=y+l*math.sin(phi)*math.sin(theta)
		    		z=z+l*math.cos(phi)

			    	x=x+dx
			    	y=y+dy
			    	z=z+dz
			    	
			    	Engergy =energy_updater(Energy)
			    	
				elif reaction_type="fission":
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2)
						theta.append("""i have to write the formula """)
						phi.append("""i have to write the formula """)
						
					
					alive=False 
				else:
					alive=False
			#5th layer 
        			 
        		if math.sqrt(x**2+y**2+z**2)>radius_clad and math.sqrt(x**2+y**2+z**2) <radius_clad2:
			 
			#that means the neutron is inside the core 
				
			sigma_s=scattering_cross_section("core")
			sigma_f=absorbtion_cross_section("core")
			sigma_f=fission_cross_section("core")
				
			total_sigma=sigma_s+sigma_f+sigma_a
			
			reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma)
				
				#need to figure out how to make a bias here 
				
			if reaction_type =="scattering":
				
				l= -math.log(1-random parameter)/(scatting_cross_section("scattering")+scatting_cross_section("scattering")	+scatting_cross_section("scattering"))

				theta=random.uniform(0,360)
				phi=random.uniform(0,180)
				x=x+l*math.sin(phi)*math.cos(theta)
		    		y=y+l*math.sin(phi)*math.sin(theta)
		    		z=z+l*math.cos(phi)

			    	x=x+dx
			    	y=y+dy
			    	z=z+dz
			    			
			    	Engergy =energy_updater(Energy)
			    	
				elif reaction_type="fission":
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2)
						theta.append("""i have to write the formula """)
						phi.append("""i have to write the formula """)
						
					
					alive=False 
				else:
					alive=False
					
			#6th layer 
        			 
        		if math.sqrt(x**2+y**2+z**2)>radius_clad and math.sqrt(x**2+y**2+z**2) <radius_clad2:
			
			#that means the neutron is inside the core 
				
			sigma_s=scattering_cross_section("core",Energy=Engergy)
			sigma_f=absorbtion_cross_section("core",Energy=Engergy)
			sigma_f=fission_cross_section("core",Energy=Engergy)
				
			total_sigma=sigma_s+sigma_f+sigma_a
			
			reaction_type=np.random.choice(["fission","scattering","absorbtion"],p=[sigma_f/total_sigma,sigma_s/total_sigma,sigma_a/total_sigma)
				
				#need to figure out how to make a bias here 
				
			if reaction_type =="scattering":
				
				l= -math.log(1-random parameter)/(scatting_cross_section("scattering")+scatting_cross_section("scattering")	+scatting_cross_section("scattering"))

				theta=random.uniform(0,360)
				phi=random.uniform(0,180)
				x=x+l*math.sin(phi)*math.cos(theta)
		    		y=y+l*math.sin(phi)*math.sin(theta)
		    		z=z+l*math.cos(phi)

			    	x=x+dx
			    	y=y+dy
			    	z=z+dz
			    	
			    	Engergy =energy_updater(Energy)
			    	
				elif reaction_type="fission":
					
					reproduction_prob=[1,2,3,4]
					new_neutron=np.random.choice(reproduction_prob,p=[0.1,0.4,0.4,0.1])
					new_gen_neutron[j]=new_gen_neutron[j]+new_neutron
					
					#location has to be saved for new initiation 
					#there will be a loop to create the same location in a matrix
					#for the same number of neutron 
					
					for k in range(new_neutron):
						r.append(math.sqrt(x**2+y**2+z**2)
						theta.append("""i have to write the formula """)
						phi.append("""i have to write the formula """)
						
					
					alive=False 
				else:
					alive=False
              

