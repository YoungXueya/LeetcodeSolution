class Solution:
    # O(b) time
    # if previous sum<0, start a new subarry
    def maxSubArray(self, nums: List[int]) -> int:
        res=-sys.maxsize-1
        temp=0
        for i in range(len(nums)):
            temp=nums[i]+(0 if temp<0 else temp)
            res=max(temp,res)
        return res
            
        
