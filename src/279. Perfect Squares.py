class Solution:
    _dp = [0]
    def numSquares(self, n):
        # dp = [sys.maxsize for i in range(1+n)]
        # dp[0]=0
        dp=self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
                
