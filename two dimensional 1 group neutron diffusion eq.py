"""importing necessary libaries """
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator


"""constants loding """
D_water=0.4
D_fuel=0.35

neu_sigma_f=0.22
sigma_a_fuel=0.18
sigma_a_water=0.05

#I have used these constants for thermal neutrons.my geometry will be surrounded by water

"""reactor core length =x_length=y_length 
thats why I think there is no need to initiliaz another variable for y_length since I am working with square mesh  """

x_length=10

mesh_size=1
external_source=10
total_mesh=int(x_length/mesh_size)
size_of=0.1

def top_point(i,j):
    
    if (i/(total_mesh+1)**2 > size_of and  i/(total_mesh+1)** 2< (1-size_of)) and (j /(total_mesh+1)**2 > size_of and i/(total_mesh+1)**2< (1-size_of)):

        return -D_fuel/mesh_size**2
    else:
        return -D_water/mesh_size**2


def right_point(i,j):
    
    if (i/(total_mesh+1)**2 > size_of and  i/(total_mesh+1)** 2< (1-size_of)) and (j /(total_mesh+1)**2 > size_of and i/(total_mesh+1)**2< (1-size_of)):

        return -D_fuel/mesh_size**2
    else:
        return -D_water/mesh_size**2


def bottom_point(i,j):
    
    if (i/(total_mesh+1)**2 > size_of and  i/(total_mesh+1)** 2< (1-size_of)) and (j /(total_mesh+1)**2 > size_of and i/(total_mesh+1)**2< (1-size_of)):

        return -D_fuel/mesh_size**2
    else:
        return -D_water/mesh_size**2


def left_point(i,j):
    
    if (i/(total_mesh+1)**2 > size_of and  i/(total_mesh+1)** 2< (1-size_of)) and (j /(total_mesh+1)**2 > size_of and i/(total_mesh+1)**2< (1-size_of)):

        return -D_fuel/mesh_size**2
    else:
        return -D_water/mesh_size**2

def main_point(i,j):
    
    if (i/(total_mesh+1)**2 > size_of and  i/(total_mesh+1)** 2< (1-size_of)) and (j /(total_mesh+1)**2 > size_of and i/(total_mesh+1)**2< (1-size_of)):
        
        """fuel region """
        #need to convert this indexing into the meshing data point.
        #but if i do FDM then there is no need of it 
        #will be recreating this result again using fvm
        
        return 4*D_fuel/mesh_size**2+sigma_a_fuel-neu_sigma_f
    else: 
        return  4*D_fuel/mesh_size**2+sigma_a_water

def constant_vector ():
    constant_vector=np.zeros(int((1+total_mesh)**2))
    constant_vector[:]=external_source
    return constant_vector
     



"""matrix creation """

def create_matrix():
    a=int ((total_mesh+1)**2)
    matrix=np.zeros((a,a) )

    #"""matrix formation is OK.but it will bother about the meshing.Need to work on it again """ 
    #this problem is fixed now.The code is OK  

    for i in range (a):
        for j in range (a):
            if i==j:
                matrix[i][j]=main_point(i,j)
                try:
                    matrix[i+1][j]=left_point(i+1,j)
                    matrix[i-1][j]=right_point(i-1,j)
                except:
                    pass
                
            
    matrix[total_mesh][-1]=right_point(total_mesh,total_mesh)

    for i in range(a):
        for j in range (a):
            if i==j:
                if i%(total_mesh+1)==0:
                    matrix[i-1][j]=0
                    try:
                        matrix[i][j-1]=0
                    except:
                        pass
    for i in range(a):
        """ x_mesh gorverning variable is i """

        for j in range (a):
            """ y_mesh gorverning variable is j """

            #ffs
            """bottom condition i-j=total mesh"""
            if i-j==(total_mesh+1):
                matrix[i,j]=bottom_point(i,j)
               

            """top point condition i-j=total mesh"""
            if j-i==(total_mesh+1):
                matrix[i][j]=top_point(i,j)

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
        
""" linear system solving """        
matrix=create_matrix()
constant_vector=constant_vector()
phi=solver(matrix,constant_vector,epsilon=0.01)

""" preparing the data for graph generation """

x=np.arange(0,total_mesh+1)
y=np.arange(0,total_mesh+1)
X,Y=np.meshgrid(x,y)
phi=phi.reshape(total_mesh+1,total_mesh+1)

""" graph generation """

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
xLabel = ax.set_xlabel('X-axis', linespacing=.21)
yLabel = ax.set_ylabel('Y-axis', linespacing=.1)
surf = ax.plot_surface(X, Y, phi, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
