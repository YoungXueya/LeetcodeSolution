class Solution:
    # Hera are some tricks that binary seach tree has order.
    # if 2 as root, then there are only 1 in the left and (n-2) in the right
    # So the combination of number of left and right is the number of 2 as root.
    
    def numTrees(self, n: int) -> int:
        dp=[0 for dp in range(n+1)]
        dp[0]=dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]
