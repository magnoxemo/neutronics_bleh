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

def create_matrix_neu_f(group_number,cross_section="neu_F"):

    cross_section=cross_section 
    group_number=group_number

    if cross_section=='neu_F':
        matrix=np.zeros(total_mesh+1,total_mesh+1)

        for i in range (total_mesh+1):
            for j in range (total_mesh+1):
                if i==j:
                    matrix[i][j]=neu_fission_cross_section(i,group_number)
    
    return matrix

def create_matrix_sigma_s(group_number,cross_section):

    cross_section=cross_section 
    group_number=group_number

    if cross_section=="sigma_s":
        matrix=np.zeros(total_mesh+1,total_mesh+1)

        for i in range (total_mesh+1):
            for j in range (total_mesh+1):
                if i==j:
                    matrix[i][j]=scattering_cross_section(i,group_number)
    
    return matrix
def group_1_solver(k,flux1,flux2,fission_flux1,fission_flux2,scattering_flux):
    a=np.matmul(fission_flux1,flux1)
    b=np.matmul(fission_flux2,flux2)
    c=np.matmul(scattering_flux,flux2)
    rhs=1/k(a+b)+c

    phi1=np.matmul(np.linalg.inv(flux1),rhs)

    return rhs

def group_2_solver(flux1,flux2,scattering_fulx):

    rhs=np.matmul(scattering_fulx,flux1)
    phi2=np.matmul(np.linalg.inv(flux2),rhs)
    return phi2

def k_solver(k0,phi10,phi20,phi11,phi21,flux1,flux2,fission_flux1,fission_flux2):
    x_1=np.matmul(fission_flux1,phi11)
    y_1=np.matmul(fission_flux2,phi21)
    x_0=np.matmul(fission_flux1,phi10)
    y_0=np.matmul(fission_flux2,phi20)

    k=k0*((np.sum(x_1)+np.sum(y_1))/(np.sum(x_0)+np.sum(y_0)))
    print(k)

    return (k-k0)/k

