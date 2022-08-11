import numpy as np
matrix=np.zeros((16,16))

"""matrix formation is OK.but it will bother about the meshing.Need to work on it again """

for i in range (16):
    for j in range (16):
        if i==j:
            matrix[i][j]=
            try:
                matrix[i+1][j]=2
                matrix[i-1][j]=4
            except:
                pass
            
matrix[14][-1]=4

for i in range(16):
    for j in range (16):
        if i==j:
            if i%4==0:
                matrix[i-1][j]=0
            if i%4==0:
                try:
                    matrix[i][j-1]=0
                    
                except:
                    pass
