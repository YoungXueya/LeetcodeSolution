class Solution:
    # O(log(n^2)) 
    # refer to https://www.youtube.com/watch?v=CE2b_-XfVDk
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest=[1 for i in range(len(nums))]
        count=1
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    longest[i]=max(longest[j]+1,longest[i])
                    
                    count=max(count,longest[i])
             
        return count if nums else 0
        
