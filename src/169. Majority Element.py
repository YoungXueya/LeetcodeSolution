class Solution:
    # moore voting
    # subtract a pair of numbers that are not equal.
    # the one that last is the majority.
    def majorityElement(self,nums: List[int]) -> int:
        count,m=0,nums[0]
        for item in nums:
            if count==0:
                m=item
                count+=1
            elif m==item:
                count+=1
            else:
                count-=1
        return m
        
    def majorityElement1(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for item in dic:
            if dic[item]>len(nums)/2:
                return item
        return -1
        
