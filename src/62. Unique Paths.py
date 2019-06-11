class Solution:
    # Dynamic progrmming
    # Every current position can be achieved by from left to here or bottom to here.
    def uniquePaths(self, m: int, n: int) -> int:
        mat=[[]]
        for i in range (m):
            mat[0].append(1)
        for j in range(1,n):
            mat.append([1])
        print(mat)
        for i in range(1,m):
            for j in range(1,n):
                mat[j].append(mat[j][i-1]+mat[j-1][i])
               
        
        return mat[n-1][m-1]
    
    # Combination(N, k) = n! / (k!(n - k)!)
    def uniquePaths1(self, m: int, n: int) -> int:
        res=1
        N=m+n-2
        k=min(n-1,m-1)
        for i in range(1,k+1):
            res=res*(N-k+i)/i
        return int(res)
        
