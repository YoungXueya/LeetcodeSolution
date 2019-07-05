class Solution(object):
    
    def missingNumber(self, nums):
        Set=set()
        for item in nums:
            Set.add(item)
        for i in range(len(nums)+1):
            if i not in Set:
                return i
    # Mathematics is great!   
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)        
        return n*(n+1)/2-sum(nums)
        
