class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        countend=[0 for x in range(N+1)]
        
        for i in range(len(trust)):
            countend[trust[i][0]]-=1
            countend[trust[i][1]]+=1
        for i in range(1,N+1):
            if countend[i]==N-1:
                return i
                      
        return -1
