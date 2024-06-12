class Zcylinder():
    
    def __init__(self,x0:float,y0:float,radius:float):
        self.x0=x0
        self.y0=y0
        self.r=radius
        
    def particle_position_confirm(self,x,y,z):        
        val=(x-self.x0)**2+(y-self.y0)**2-self.r**2
        return val


class  Cell():
    def __init__(self,surface_array:list,indicator_array:list):
        """
           surface array will contain object of surface class.
           indicator array will contain logic like : inside,outside and on_the_surface. 
           the suface and the indicator array needs to be in the same order.     
        """
        self.surfaces=surface_array
        self.logic_array=indicator_array
        self.cell_id_number=self.logic_array_to_id_number()

    def logic_array_to_id_number(self):
        #id number will follow a three digit indicator 
        # 1 outside 
        # 0 inside and on the surface 
        id=[]
        for i in self.logic_array:
            if i=='inside' or i=='on_the_surface':
                id.append(0)
            elif i=='outside':
                id.append(1)

        return id 

    def particle_within_this_cell(self,r:list):
        x=r[0]
        y=r[1]
        z=r[2]
        generated_id_number=[]

        for _ in self.surfaces:
            if _.particle_position_confirm(x,y,z)<0 or _.particle_position_confirm(x,y,z)==0:
                generated_id_number.append(0)
            elif _.particle_position_confirm(x,y,z)>0:
                generated_id_number.append(1)

        """ 
        here we need a converter program which will tell us if the co ordinate is inside or outside 
        after reading the generated number 
        """
        if generated_id_number==self.cell_id_number:
            
            print("particle found in this cell ")      
            return 1
        else:
            return 0
