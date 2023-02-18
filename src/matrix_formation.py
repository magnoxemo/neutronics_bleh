def create_matrix():
    a=int ((total_mesh+1)**2)
    matrix=np.zeros((a,a),dtype=int )

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
        for j in range (a):
            """bottom condition i-j=total mesh"""
            if i-j==(total_mesh+1):
                matrix[i,j]=bottom_point(i,j)
            if j-i==(total_mesh+1):
                matrix[i][j]=top_point(i,j)

    return matrix 
