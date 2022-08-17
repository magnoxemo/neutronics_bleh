
##########################################################this code has bug ##########################################################
################# I will fix it later after i figure it out what the hell is wrong with it ############################################
####################################### but my initial guess is I used the wrong constants ############################################
################################# OK. the code is OK. The problem was I was using smaller mesh size and larger convergence value""""""
""""""""""""""""""""""it should have been smaller mesh size and much smaller convergence value """""""""""""""""""""""""""""""""""
import math 
import numpy as np
import time 
import matplotlib.pyplot as plt 


""" constant values """
D_water=1.4
D_fuel=.35

neu_sigma_f=.24
sigma_a_fuel=1.18
sigma_a_water=0.3
mesh_size=0.1
external_source=100
length=10
total_mesh=int(length/mesh_size)
"""constants are loaded """



""" necessary functions """


def constant_vector(size_of=0.1):

    constant_vector=np.zeros(int(total_mesh+1))

    constant_vector[0:int(size_of*total_mesh)]=external_source*mesh_size
    constant_vector[int((size_of)*total_mesh):]= external_source*mesh_size

    return constant_vector


def source_external(mesh_position,size_of=0.1 ):
    
    if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
        return external_source
    else: 
        return 0


def diffusion_coefficient(mesh_position,size_of=0.1):

    if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
        return D_water
    else: 
        return D_fuel


def absorbtion_cross_section(mesh_position,size_of=0.1):

    if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:

        return float(sigma_a_water)

    else: 

        return float(sigma_a_fuel)

def fission_crossection(mesh_position,size_of=0.1):

    if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
        
        return 0

    else:

        return neu_sigma_f




def create_matrix():

    total_mesh=int(length/mesh_size) 
    matrix=np.zeros((total_mesh+1,total_mesh+1))

    for i in range(1,total_mesh):
        for j in range(1,total_mesh):

            if i==j:
                matrix[i][j]=diffusion_coefficient(i)/mesh_size+diffusion_coefficient(i+1)/mesh_size
                +((absorbtion_cross_section(i)+absorbtion_cross_section(i+1)))*mesh_size/2
                -(fission_crossection(i)+fission_crossection(i+1))*mesh_size/2
                
                matrix[i][j-1]=-diffusion_coefficient(i)/mesh_size
                matrix[i][j+1]=-diffusion_coefficient(i+1)/mesh_size
    
    matrix[0][0]=diffusion_coefficient(1)/mesh_size+diffusion_coefficient(1+1)/mesh_size
    (absorbtion_cross_section(1)+absorbtion_cross_section(1+1))*mesh_size/2-(fission_crossection(1)+fission_crossection(1+1))*mesh_size/2

    matrix[total_mesh][total_mesh]=diffusion_coefficient(total_mesh+1)/mesh_size+diffusion_coefficient(total_mesh+1+1)/mesh_size
    +(absorbtion_cross_section(total_mesh+1)+absorbtion_cross_section(total_mesh+1+1))*mesh_size/2-(fission_crossection(total_mesh+1)+
    fission_crossection(total_mesh+1+1))*mesh_size/2

    matrix[total_mesh][total_mesh-1]=-diffusion_coefficient(i)/mesh_size

    matrix[0][1]=-diffusion_coefficient(1+1)/mesh_size

    return matrix
                            


def solver (matrix,constant_vector,epsilon,initial_guess=None,over_relaxation_factor=1.06):

    """checking if the linear system has any solutions """

    if np.linalg.det(matrix)!=0:

        matrix=matrix
        b=constant_vector
        epsilon=epsilon
        omega=over_relaxation_factor

        if initial_guess==None:

            x1=np.zeros(len(b))

        else:
            x1=initial_guess

        x2=np.zeros(len(b))

        m,n=np.shape(matrix)
        
        iteration=0
        c=0
        logic=False

        while logic==False:
            iteration=iteration+1
            for i in range(m):
                sum=0
                for j in range(n):
                    if i!=j:
                        sum=sum+matrix[i][j]*x1[j]
                x2[i]=((b[i]-sum)*omega/matrix[i][i])+(1-omega)*x1[i]
                x1[i]=x2[i]
            convergence=abs (np.linalg.norm(x2)-c)/np.linalg.norm(x2)
            c=np.linalg.norm(x1)
            if convergence<epsilon:
                logic=True
            print(convergence)
            
        print(iteration)
        return x1
    else:
        print("solution of this matrix is not available ")


matrix=create_matrix()
constant_vector=constant_vector()

phi=solver(matrix,constant_vector,epsilon=10**-3)

x=np.arange(0,total_mesh+1)
plt.figure(figsize=(10,6))
plt.plot(x,phi,color="green")
plt.xlabel("mesh position")
plt.ylabel("Neutron Flux")

plt.show()
