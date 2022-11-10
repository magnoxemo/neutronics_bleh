mport matplotlib.pyplot as plt 
import numpy as np 

class geometry():
    def __init__(self):
        pass 
    
    def add_material(self,material,r
                     
                     #more will be updated adius):
        self.material=material
        self.radius=radius

    def graph(self,colo):
        radius=np.array(self.radius)
        colo=colo
        circle=[]
        for i in range (len(radius)):
            circle.append(plt.Circle((0,0),radius[i],color=colo[i],fill=False))
            plt.gca().add_patch(circle[i])
        plt.axis("scaLed")
        plt.show()


r=[1,1.02,1.5,1.7,2,2.1]
material=['u','h2','d20','be02','d2o','ad']
color=['red','green','blue','pink','blue','green']

sim=geometry()
sim.add_material(material,r)
sim.graph(color)

#more will be updated 
