class Solution:
    # From start to the end
    def canJump(self, nums: List[int]) -> bool:
        maxStep=0
        for i in range(len(nums)):
            if i>maxStep:
                return False
            maxStep=max(i+nums[i],maxStep)
        return True
    # From end to the start 
    def canJump(self, nums: List[int]) -> bool:
        lastPos=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i>=lastPos:
                lastPos=i
        return lastPos==0
        
