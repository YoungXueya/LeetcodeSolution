class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        print(dp)
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
            # Judge if two character are equal, if equal, add one based on the previous result.
            # Otherwise, Select the maximum one back one character in one string. 
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(text1)][len(text2)]
