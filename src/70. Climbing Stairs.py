class Solution:
    def climbStairs(self, n: int) -> int:
        dp1=1
        dp2=2
        dpway=0
        if(n==1):
            return dp1
        if(n==2):
            return dp2
        while n-2>0 :
            dpWay=dp1+dp2
            dp1=dp2
            dp2=dpWay
            n-=1
        return dp2
    
    # A easier understanding way
    # The N stair can be achived by step one on the base of n-1 or step 2 on n-2.
    # So this is the reason that dp[i]=dp[i-1]+dp[i-2]
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        if n==1:
            return 1
        if n==2:
            return 2
        dp[1],dp[2]=1,2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
