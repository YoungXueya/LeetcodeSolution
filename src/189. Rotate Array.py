class Solution(object):
    # This is amazing, The result can be infered from list the reverse result.
    # Origin [1,2,3,4,5,6,7]
    # First reverse [7,6,5,4,3,2,1]
    # First half reverse [5,6,7,4,3,2,1]
    # Last half reverse [5,6,7,1,2,3,4]
    # Remember to k=k % len(nums)
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(nums,0,len(nums)-1)
       
        self.reverse(nums,0,k-1)
        
        self.reverse(nums,k,len(nums)-1)
      
    
    def reverse(self,nums,start,end):
        while(start<end):
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
        
