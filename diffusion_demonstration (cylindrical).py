def diffusion(): 
    #importing necessary libraries for calculation
    # and ploting  
    import math 
    import random 
    import matplotlib.pyplot as plt 
    from mpl_toolkits.mplot3d import Axes3D

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    
    #defining atom density ,cross section for scattering and absorption

    atom_density=9.085*10**22
    sigma_s=20*10**-24
    sigma_a=0.2*10**-24
    lemda_s=1/(atom_density*sigma_s)
    lemda_a=1/(atom_density*sigma_a)

    #rechecking the values if they are OK for calcultaion because there 
    # will be no reactor of height of 0 and no diffusion if there is no neutrons 

    
        
        #intilizing co-ordinates for neutrons
    x=[]
    y=[]
    z=[]

    height=int(input("Enter the height of the reactor:"))
    n=int(input('Enter the number of the neutrons: '))

    def point_source():
        
        x=0
        y=0
        z=random.uniform(-float(height/2),float(height/2))

        while True :

            a=random.uniform(0,1)

            if a>=0 and a<=sigma_s/(sigma_s+sigma_a):

                theta=random.uniform(0,360)
                phi=random.uniform(0,180)

                dx=lemda_s*math.cos(phi)*math.cos(theta)
                dy=lemda_s*math.cos(phi)*math.sin(theta)
                dz=lemda_s*math.sin(phi)

                x=x+dx
                y=y+dy
                z=z+dz
            
            else:
                copy=[x,y,z]

                return copy

    for i in range (n):
        copy=point_source()
        x.append(copy[0])
        y.append(copy[1])
        z.append(copy[2])
    
    #ploting the graph 

    ax.scatter(x,y,z,c='red',marker='.')
    ax.set_xlabel("x- axis")
    ax.set_ylabel("y- axis")
    ax.set_zlabel("z- axis")

    plt.show()

diffusion()
