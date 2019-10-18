class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=self.binarySearch(nums,target)
        
        if index==-1 or not nums:
            return [-1,-1]
        l = r = index
        print(index)
        while l >= 0 and nums[l] == target:
            l -= 1
        while r < len(nums) and nums[r] == target:
            r += 1
        
        return [l+1, r-1]
        
    def binarySearch(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[left]==target:
                return left
            if nums[right]==target:
                return right
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            
        return -1
                
        
