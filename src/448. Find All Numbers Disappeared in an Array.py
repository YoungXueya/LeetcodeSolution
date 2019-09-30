class Solution:
    # If the number appears, mark it as negative,
    # For the consideration of overflow, 
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [i+1 for i in range(len(nums)) if nums[i]>0]
        
