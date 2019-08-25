class NumArray:
    #Using Hash map is quicker than using a cumulative array
    def __init__(self, nums: List[int]):
        self.result={}
        self.result[-1]=0
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            self.result[i]=sum
             
    def sumRange(self, i: int, j: int) -> int:
        return self.result[j]-self.result[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
