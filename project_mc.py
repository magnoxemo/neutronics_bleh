import random
import pandas as pd 
import numpy as np
import math

"""
this is the first attempt to write a monte carlo code for a spherical nuclear reactor.In this attempt i will not be keeping tracks of the energy distribution.
this code will solve the eigenvalues which will be computed using the formula 

					keff=(number of neutrons in i+1 gen)/ ( number of neutrons in i th gen)  
					
As I am doing this for a single group of neutrons no maxwell boltzman energy distribution is needed.

##################################################################################################################################################################

steps:

1.random samplaing the location of initial position of neutron and moving it, saving those location.
						
						#########    moving calculation   ################
						
						from point A ------> point B
moving will happen spherical co ordinates.so (R_a,theta_a,phi_a)--------> (R_b,theta_b,phi_b).
						
we will be using spherical co ordinates [r,theta,phi]

2.Distance travel will happen using this formula 

					l= -math.log(1-random parameter)/total_Sig_t
				

and then random values for						  
						  
						   theta ->[-pi,+pi]
						   phi   ->[-pi/2,+pi/2]
			
3.check for the probability for each possible type of cases.

				a) new neutron will generate if fission happens 
					
					subcases:
						[i]    neutron alive=False 
						[ii]   randomly the number of the promt neutron will be counted from the guess 
							guess->[1,2,3,4].and there will be probability bias 
						[iii]  have to save the location of new born neutron for next gen calculation 
						[iv]   keep count the number of the prompt neutron 
						
						
				b)direction will alter if scattering happens 
				c)neutron will alive=False if absorbtion happens  
				d)leakage alive =False 
				
4.repeat those process for the all nth gen neutron 
5.calculate eigenvalue 
6.show it in a graph with respect with gen which will give a competetive understanding if the reactor is critical or not. 


#######################################################################################################################################################################
copy right :

Ibne Walid Ahammed 
Dept of Nuclear Engineering 
University of Dhaka 
		 
"""
"""necessary function """

def scatting_cross_section(neutron_energy):

	#there will csv cross section data file from where data will be calculated 
	
	pass 
	return energy

def absorbtion_cross_section(neutron_energy):

	#there will csv cross section data file from where data will be calculated
	pass 
	return energy
	
def fission_cross_section(neutron_energy):

	#there will csv cross section data file from where data will be calculated
	pass
	return energy 

def material_composition():

	pass 
								
								"""necessary data loading """


radius_core=
number_of_neutron=10**6
sigma_a=
sigma_f=
sigma_s=

sigma_total=sigma_a+sigma_f+sigma_s 
inv_sigma_total=1/sigma_total
							      """initial position distribution"""
							      
position_matrix=np.zeros((number_of_neutrons,3))

for i in range (number_of_neutrons_):
	position_matrix[i][0]=np.random.uniform(0,r)                      #radius record 
	position_matrix[i][1]=np.random.uniform(-np.pi,np.pi)             #theta record 
	position_matrix[i][2]=np.random.uniform(-np.pi/2,np.pi/2)	  #phi record 
	
	

for i in range (number_of_neutrons):

        
        while alive:
        
        	if math.sqrt(x**2+y**2+z**2)<radius_core:
        		sigma_s=scattering_cross_section()
        		sigma_f=absorbtion_cross_section()
        		sigma_f=fission_cross_section()
        		
        		reaction_type=random.random(["fission","scattering","absorbtion"]) #need to figure out how to make a bias here 
