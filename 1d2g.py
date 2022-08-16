import math 
import numpy as np
import time 
import matplotlib.pyplot as plt 


""" constant values """
D_water_1=1.1245305
D_water_2=0.7503114

D_fuel_1=1.0933622
D_fuel_2=.3266693

neu_sigma_f_1=.24
neu_sigma_f_2=.24

sigma_a_fuel_1=0.0092144
sigma_a_fuel_2=0.0778104

sigma_f_fuel_1=0.0092144
sigma_f_fuel_2=0.0778104

sigma_a_water_1=0.0008996
sigma_a_water_2=0.0255590

sigma_s_fuel_1=0.0181930
sigma_s_fuel_2=0.0013089

sigma_s_water_1=0.0255380
sigma_s_water_2=0.0001245

"""constants are loaded """

mesh_size=0.1
external_source=10
length=10
total_mesh=int(length/mesh_size)


""" necessary functions """


def constant_vector(group_number,size_of=0.1):
    constant_vector=np.zeros(int(total_mesh+1))
    if group_number==1:

        """bleh bleh bleh """
    if group_number==2:

        """bleh bleh bleh """

    ##


def source_external(mesh_position,group_number,size_of=0.1 ):
    
    #external source of neutron will be fast neutron 

    if group_number==1:
        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
            return external_source
        else: 
            return 0
    else:
        return 0


def diffusion_coefficient(mesh_position,group_number,size_of=0.1):

    if group_number==1:
        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
            return D_water_1
        else: 
            return D_fuel_1
    if group_number==2:
        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
            return D_water_2
        else: 
            return D_fuel_2
    


def absorbtion_cross_section(mesh_position,group_number,size_of=0.1):

    if group_number==1:

        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:

            return float(sigma_s_water_1)

        else: 

            return float(sigma_s_fuel_1)

    if group_number==2:

        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:

            return float(sigma_s_water_2)

        else: 

            return float(sigma_s_fuel_2)


def neu_fission_cross_section(mesh_position,group_number,size_of=0.1):

    if group_number==1:
        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
        
            return 0

        else:

            return neu_sigma_f_1

    if group_number==2:
        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:
        
            return 0

        else:

            return neu_sigma_f_2


def scattering_cross_section(mesh_position,group_number,size_of=0.1):

    if group_number==1:

        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:

            return float(sigma_a_water_1)

        else: 

            return float(sigma_a_fuel_1)
    if group_number==2:

        if mesh_position< size_of*total_mesh or mesh_position>(1-size_of)*total_mesh:

            return float(sigma_a_water_2)

        else: 

            return float (sigma_a_fuel_2)


def create_matrix_phi(group_number):

    total_mesh=int(length/mesh_size) 
    matrix=np.zeros((total_mesh+1,total_mesh+1))
    group_number=group_number

    for i in range(1,total_mesh):
        for j in range(1,total_mesh):

            if i==j:
                matrix[i][j]=diffusion_coefficient(i,group_number)/mesh_size
                +diffusion_coefficient(i+1,group_number)/mesh_size
                +((absorbtion_cross_section(i,group_number)
                +absorbtion_cross_section(i+1,group_number)))*mesh_size/2
                #-(fission_cross_section(i,group_number)
                #+fission_cross_section(i+1,group_number))*mesh_size/2
                
                matrix[i][j-1]=-diffusion_coefficient(i,group_number)/mesh_size
                matrix[i][j+1]=-diffusion_coefficient(i+1,group_number)/mesh_size
    
    #boundary conditions 

    matrix[0][0]=diffusion_coefficient(1,group_number)/mesh_size
    +diffusion_coefficient(1+1,group_number)/mesh_size
    (absorbtion_cross_section(1,group_number)
    +absorbtion_cross_section(1+1,group_number))*mesh_size/2
    #-(fission_cross_section(1,group_number)
    #+fission_cross_section(1+1,group_number))*mesh_size/2

    matrix[total_mesh][total_mesh]=diffusion_coefficient(total_mesh+1,group_number)/mesh_size
    +diffusion_coefficient(total_mesh+1+1,group_number)/mesh_size
    +(absorbtion_cross_section(total_mesh+1,group_number)
    +absorbtion_cross_section(total_mesh+1+1,group_number))*mesh_size/2
    #-(fission_cross_section(total_mesh+1,group_number)+
    #fission_cross_section(total_mesh+1+1,group_number))*mesh_size/2

    matrix[total_mesh][total_mesh-1]=-diffusion_coefficient(i,group_number)/mesh_size

    matrix[0][1]=-diffusion_coefficient(1+1,group_number)/mesh_size

    #end of matrix formation 

    return matrix

def create_matrix_neu_f(group_number,cross_section):

    cross_section=cross_section 
    group_number=group_number

    if cross_section=='neu_F':
        matrix=np.zeros(total_mesh+1,total_mesh+1)

        for i in range (total_mesh+1):
            for j in range (total_mesh+1):
                if i==j:
                    matrix[i][j]=neu_fission_cross_section(i,group_number)

    if cross_section=="sigma_s":
        matrix=np.zeros(total_mesh+1,total_mesh+1)

        for i in range (total_mesh+1):
            for j in range (total_mesh+1):
                if i==j:
                    matrix[i][j]=neu_fission_cross_section(i,group_number)
    
    return matrix

def create_matrix_sigma_s(group_number,cross_section):

    cross_section=cross_section 
    group_number=group_number

    if cross_section=='neu_F':
        matrix=np.zeros(total_mesh+1,total_mesh+1)

        for i in range (total_mesh+1):
            for j in range (total_mesh+1):
                if i==j:
                    matrix[i][j]=scattering_cross_section(i,group_number)

    if cross_section=="sigma_s":
        matrix=np.zeros(total_mesh+1,total_mesh+1)

        for i in range (total_mesh+1):
            for j in range (total_mesh+1):
                if i==j:
                    matrix[i][j]=scattering_cross_section(i,group_number)
    
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
            convergence=abs (x2[2]-c)/x2[2]
            c=x2[2]
            print(convergence)
            if convergence<epsilon:
                logic=True
            
        print(iteration)
        return x1
    else:
        print("solution of this matrix is not available ")
