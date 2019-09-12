class Solution:
    def fib(self, N: int) -> int:
        prev2=0
        prev1=1
        if N==0:
            return 0
        if N==1:
            return 1
        for i in range(2,N+1):
            cur=prev2+prev1
            prev1,prev2=cur,prev1
        return cur
