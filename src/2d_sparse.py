import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import time

"""constants loding """
D_water=2.4
D_fuel=2.35

neu_sigma_f=0.22
sigma_a_fuel=0.18
sigma_a_water=0.05

x_length=4

mesh_size=0.1
external_source=1
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

    """matrix formation is OK.but it will bother about the meshing.Need to work on it again """ 

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
def gauss_seidel_sparse_solver(A, b, x,epsilon):
  initial_guess=x
  epsilon=epsilon
  x1=np.zeros_like(initial_guess)
  m,n=np.shape(A)
  cnt=0
  
  while True:
    i=0
    cnt=cnt+1
    start=time.time()
    while i<m:
      sum=0
      flag=int(A[i][0])
      while True:
        if i>=m or flag!=A[i][0]:
          break
        if A[i][0]!=A[i][1]:
          sum=sum+A[i][2]*initial_guess[int(A[i][1])]
          
        else:
          div=A[i][2]
        i=i+1
      
      x1[int(flag)]=((b[int(flag)]-sum)/div)

    convergence=abs (np.linalg.norm(x1)-np.linalg.norm(initial_guess))/np.linalg.norm(x1)
    initial_guess=x1.copy()
    if cnt%100==0:
    	end=time.time()
    	print(f'\n\nIteration number {cnt} --- time: {-start+end}\nConvergence:',convergence)

    #break
    if convergence<epsilon:
      break
    initial_guess=x1.copy()
  
  print('total interation ',cnt)
  return x1
  
def sparse_converter(matrix):
  m,n=np.shape(matrix)
  row=[]
  col=[]
  val=[]
  for i in range(m):
    for j in range(n):
      if matrix[i][j]!=0:
        row.append(i)
        col.append(j)
        val.append(matrix[i][j])
  return row,col,val
  
matrix=create_matrix()

row,col,val=sparse_converter(matrix)
new_matrix=np.column_stack((row,col,val))


def constant_vector ():
    constant_vector=np.zeros(int((1+total_mesh)**2))
    constant_vector[:]=external_source
    return constant_vector
    
    
constant_vector=constant_vector()
initial_guess=np.zeros_like(constant_vector)
phi=gauss_seidel_sparse_solver(A=new_matrix,b=constant_vector,x=initial_guess,epsilon=10**-6)

x=np.arange(0,total_mesh+1)
y=np.arange(0,total_mesh+1)
X,Y=np.meshgrid(x,y)
phi=phi.reshape(total_mesh+1,total_mesh+1)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, phi, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
