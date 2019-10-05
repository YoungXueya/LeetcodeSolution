class Solution:
    # 2 is always enough, therefore, count number of 5
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n!=0:
            n=n//5
            count+=n
        return count
