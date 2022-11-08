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


"""necessary data loading """

radius_core=3
number_of_neutron=10**6
sigma_a=1
sigma_f=1
sigma_s=1
sigma_total=sigma_a+sigma_f+sigma_s 
inv_sigma_total=1/sigma_total

"""initial position distribution"""
							      
position_matrix=np.zeros((number_of_neutrons,3))

for i in range (number_of_neutrons_):
	position_matrix[i][0]=np.random.uniform(0,r)                      #radius record 
	position_matrix[i][1]=np.random.uniform(-np.pi,np.pi)             #theta record 
	position_matrix[i][2]=np.random.uniform(-np.pi/2,np.pi/2)	  #phi record 
	
	
new_gen_neutron=0 #before the simulation 

for i in range (number_of_neutrons):

    #few things to be fixed before the neutron simulation 
    
	alive=True 
	while (alive):
        scattering_prob=np.random()
        if scattering_prob < sigma_s*inv_sigma_total:

            """random parameters generation fro scattering purposes """

            random_parameter=np.random()
            theta=np.random(-np.pi,np.pi)
            phi=np.random(-np.pi/2,np.pi/2)

            #distance calculating 

            l= -math.log(1-random_parameter)/total_Sig_t

            """moving  conditions """
            pass 
        else :
            fission_prob=np.random()
            if fission_prob <sigma_f*inv_sigma_total:
                """fission conditions and new daughter gen neutron production """
                alive=False 
                new_gen_neutron=new_gen_neutron+np.random.choice([1,2,3,4,5])
                pass 
            else: 
                #absorbtion loss
                alive=False 
