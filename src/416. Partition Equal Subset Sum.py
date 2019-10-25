class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        dp=[True]+[False]*target
        nums=sorted(nums)
        for num in nums:
            dp=[dp[i] or (i>=num and dp[i-num]) for i in range(target+1)] 
            if dp[target]:
                return True
        return False
                
            
