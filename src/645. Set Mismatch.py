class Solution:
    # O(n) time, O(n) space
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                num1=num
        for i in range(1,len(nums)+1):
            if i in s:
                continue
            else:
                num2=i
        return [num1,num2]
        
                
