def diffusion():

    import random 
    import math
    import matplotlib.pyplot as plt 
    from mpl_toolkits.mplot3d import Axes3D

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')

    # number of neutrons 

    n=int (input("how many number of neutrons "))
    distance=[]

    sigma_s=20*10**-24
    sigma_a=0.2*10**-24
    lemda_s=1/sigma_s       
    lemda_a=1/sigma_a

    x=[]
    y=[]
    z=[]

    def reaction():
        x=0
        y=0
        z=0
        while True :

            a=random.uniform(0,1)

            if a>=0 and a<=sigma_s/(sigma_s+sigma_a):
                theta=random.uniform(0,360)
                phi=random.uniform(0,180)


                dx=lemda_s*math.sin(phi)*math.cos(theta)
                dy=lemda_s*math.sin(phi)*math.sin(theta)
                dz=lemda_s*math.cos(phi)

                x=x+dx
                y=y+dy
                z=z+dz
            
            else:
                copy=[x,y,z]

                return copy

    for i in range(n):
        copy=reaction()
        x.append(copy[0])
        y.append(copy[1])
        z.append(copy[2])

        distance.append(math.sqrt(copy[0]**2+copy[1]**2+copy[2]**2))

    
    ax.scatter(x,y,z, c='green',marker='*')
    ax.set_xlabel("x- axis")
    ax.set_ylabel("y- axis")
    ax.set_zlabel("z- axis")

    mean_distance=sum(distance)/n
    print(mean_distance)

    plt.show()
diffusion()
