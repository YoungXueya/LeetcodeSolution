class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        def house_robber(nums):
            if not nums:
                return 0
            for i in range(len(nums)):
                if i==0:
                    prev2=nums[i]
                    cur=nums[i]  
                elif i==1:
                    cur=max(nums[0],nums[1])
                    prev1=cur
                else:
                    cur=max(prev2+nums[i],prev1)
                    prev2=prev1
                    prev1=cur
            return cur
        # The choice is that either not rob the first one, or the last one. Only not the same time is OK.
        # That is the maximum of [0,n-1] and [1,n]
        return max(house_robber(nums[0:len(nums)-1]),house_robber(nums[1:]))
    
       
            
