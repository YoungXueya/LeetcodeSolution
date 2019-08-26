class Solution:
    
    def dominantIndex(self, nums: List[int]) -> int:
        MAX=-1
        secondMax=-1
        index=0
        for i in range(len(nums)):
            if nums[i]>MAX:
                secondMax=MAX
                MAX=nums[i]
                index=i
            elif nums[i]>secondMax:
                secondMax=nums[i]
        if MAX>=2*secondMax:
            return index
        else:
            return -1
        
    def dominantIndex1(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums1=sorted(nums,reverse=True)
        if nums1[0]>=2*nums1[1]:
            for i in range(len(nums)):
                if nums[i]==nums1[0]:
                    return i
        else:
            return -1
                
                
