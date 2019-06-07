class Solution:
    # XOR rules:
    # 3^3=0 0^3=0
    # XOR obeys Exchange law so 0^3^1^3=0^3^3^1=1
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for x in nums:
            res=res^x
        return res
        
