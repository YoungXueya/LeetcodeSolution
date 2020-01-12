class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        dist=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        maxDist=len(matrix[0])+len(matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j]!=0:
                    up=dist[i-1][j]+1 if i>0 else maxDist
                    left=dist[i][j-1]+1 if j>0 else maxDist
                    dist[i][j]=min(up,left)      
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
            
                if matrix[i][j]!=0:
                    down=dist[i+1][j] if i<len(matrix)-1 else maxDist
                    right=dist[i][j+1] if j<len(matrix[0])-1 else maxDist
                    dist[i][j]=min(min(down,right)+1,dist[i][j])
        return dist
