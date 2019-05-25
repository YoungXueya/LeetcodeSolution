class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
      
        temp=[0]*len(A)
        odd=1
        even=0
        for i in range(len(A)):
            if A[i]%2==0:
                temp[even]=A[i]
                even+=2
            else:
                temp[odd]=A[i]
                odd+=2
        return temp
                
                
            
            
        
