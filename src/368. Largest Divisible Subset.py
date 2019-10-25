class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        res=[]
        if not nums :
            return res
        nums=sorted(nums)
        dp=[1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    dp[i]=max(dp[i],dp[j]+1)
        
        maxIndex=0
        
        for i in range(len(dp)):
            if dp[i]>dp[maxIndex]:
                maxIndex=i
        temp=nums[maxIndex]
        curDp=dp[maxIndex]
        for i in range(maxIndex,-1,-1):
            if temp%nums[i]==0 and dp[i]==curDp:
                res.append(nums[i])
                curDp-=1
        return res
        
