class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # when comes to a unvisited block, could dfs all its neighbours and count+1
        count=0
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        def dfs(i,j):
            # print(i,j)
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j]=True
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1' and not visited[i][j] :
                    dfs(i,j)
                    count+=1
        return count
        
