class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            result[i]=nums[i-1]*result[i-1]
        right=1
        for j in range(len(nums)-2,-1,-1):
            right*=nums[j+1]
            result[j]*=right
        return result
        
