class Solution(object):
    # O(n*log(n)
    # Pigeonhole principle. If there are more than mid numbers of number in the list
    # Duplicate happends in the low-->mid half.
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        
        while(low<high):
            mid=low+(high-low)/2
            count=0
            
            for i in nums:
                if i<=mid:
                    count+=1
            if count>mid:
                high=mid
            else:
                low=mid+1
        return low
                
            
        
        
        
