class Solution:
    # This is an smart solution
    # Use multiply of 1-o[i][j] to determine whether there are obstacles.
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        obstacleGrid[0][0]=1-obstacleGrid[0][0]
        for i in range(1,col):
            obstacleGrid[0][i]=obstacleGrid[0][i-1]*(1-obstacleGrid[0][i])
           
        for j in range(1,row):
            obstacleGrid[j][0]=obstacleGrid[j-1][0]*(1-obstacleGrid[j][0])         
        for i in range(1,row):
            for j in range(1,col):
                obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]
                    
                
    # Consider the first row and column, if the previous one is set 0, then the latter ones are 0 too.
    # If one is obstacle, there is no way to it.
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        mat=[[0] for i in range(row)]
        mat[0]=[0 for i in range(col)]
        for i in range(col):
             if obstacleGrid[0][i]==1:
                break
             else:
                mat[0][i]=1
        for j in range(row):
             if obstacleGrid[j][0]==1:
                break
             else:
                mat[j][0]=1             
        for i in range(1,row):
            for j in range(1,col):
               
                if(obstacleGrid[i][j])==1:
                    mat[i].append(0)
                else:
                     mat[i].append(mat[i-1][j]+mat[i][j-1])
        return mat[row-1][col-1]
