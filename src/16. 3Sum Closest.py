class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        nums.sort()
        result=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-1):
            lo,hi=i+1,len(nums)-1
            while(lo<hi):
                sum=nums[i]+nums[lo]+nums[hi]
                if(sum==target):
                    return target
                if abs(sum-target)<abs(result-target):
                        result=sum
                if(sum>target):                   
                    hi-=1
                elif (sum<target):                    
                    lo+=1  
        return result
