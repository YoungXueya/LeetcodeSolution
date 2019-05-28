class Solution:
    #Nested loops,perform bad
    def moveZeroes1(self, nums: List[int]) -> None:
        count=0
        if len(nums)<2:
            return         
        for i in range(len(nums)-1):
            if(nums[i]==0):
                j=i+1
                print(j)
                while j<len(nums)-1 and nums[j]==0:
                    j+=1
                if(j==len(nums) and nums[j]==0):
                    return
                nums[i],nums[j]=nums[j],nums[i]
                
            
    # perform relatively good, O(n) time
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[count]=nums[i]
                count+=1
        for i in range(count,len(nums)):
            nums[i]=0
            
                
