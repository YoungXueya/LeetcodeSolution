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
    
    
    def canPartition2(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        dp=[True]+[False]*target
        nums=sorted(nums)
        for num in nums:
            newDP=[False]*(target+1)
            if num>target:
                return False
            for i in range(num):
                newDP[i]=dp[i]
            for i in range(num,target+1):
                newDP[i]=dp[i] or dp[i-num]
            dp=newDP
            # print(dp)
            if dp[target]:
                return True
        return False
                
            
