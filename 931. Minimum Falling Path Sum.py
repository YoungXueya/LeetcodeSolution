class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        result=[[0 for i in range(len(A))] for i in range(len(A))]
        
        result[len(A)-1]=[A[len(A)-1][i] for i in range(len(A))]
        
        for level in range(len(A)-2,-1,-1):
            for i in range(len(A[level])):   
                temp=result[level+1][i]
                if i-1>=0:
                    temp=min(temp,result[level+1][i-1])
                if i+1<len(A):
                    temp=min(temp,result[level+1][i+1])    
                result[level][i]=temp+A[level][i]
            
        return min(result[0])
                
                
                
                
