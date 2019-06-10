class Solution:
    # Iterative with 2 variables
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if i==0:
                prev2=nums[0]
                res=prev2
            elif i==1:
                prev1=max(nums[0],nums[1])
                res=prev1
            else:
                res=max(prev1,prev2+nums[i])
                prev2=prev1
                prev1=res
                
        return res
    # Iterative with array
    def rob(self, nums: List[int]) -> int:
        res=[]
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if i==0:
                res.append(nums[0])
            elif i==1:
                res.append(max(nums[0],nums[1]))
            else:
                maxCur=max(res[i-1],res[i-2]+nums[i])
                res.append(maxCur)
        return res[len(nums)-1]
   
            
