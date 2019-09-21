class Solution:
    # Binary Search.
    # If nums[i]<nums[i+1], there is a peak in the right , left=mid+1
    # Else if nums[i]>nums[i+1], nums[i] might be the peak or not. so right=mid 
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            elif nums[mid]>nums[mid+1]:
                right=mid
        return left
     
     #Brute Force
     def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            if i==0 and nums[i]>nums[i+1]:
                return 0
            elif i==len(nums)-1 and nums[i]> nums[i-1]:
                return i
                    
            elif nums[i]> nums[i-1] and nums[i]>nums[i+1]:
                    return i
