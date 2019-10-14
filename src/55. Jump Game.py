class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxStep=0
        for i in range(len(nums)):
            if i>maxStep:
                return False
            maxStep=max(i+nums[i],maxStep)
        return True
        
