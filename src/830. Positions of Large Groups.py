class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        left=0
        right=0
        res=[]
        while left<len(S):
            while right<len(S) and S[right]==S[left]:
                right+=1
            if right-left>=3:
                res.append([left,right-1])
            left=right
            
        return res
        
