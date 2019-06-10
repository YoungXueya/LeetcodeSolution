class Solution:
    # Every island count the right and down neighbour
    # Each adjacency causes the loss of two sides.
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        island=0
        neighbour=0
       
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    island+=1
                    
                    if i+1<len(grid) and grid[i+1][j]==1:
                        neighbour+=1
                    if j+1<len(grid[i]) and grid[i][j+1]==1:
                        neighbour+=1
                    
        return island*4-neighbour*2
        
        
    # Brute-force and strightforward
    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        res=0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    temp=4
                    if i-1>=0 and grid[i-1][j]==1:
                        temp-=1
                    if j-1>=0 and grid[i][j-1]==1:
                        temp-=1
                    if i+1<len(grid) and grid[i+1][j]==1:
                        temp-=1
                    if j+1<len(grid[i]) and grid[i][j+1]==1:
                        temp-=1
                    res+=temp
        return res
                    
                        
