class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp=[0 for i in range(len(s))]
                
        dp[0]= 0 if s[0]=='0' else 1
        for i in range(1,len(s)):
            one=s[i:i+1]
            two=s[i-1:i+1]
            # If this chararcter can be convert individually, then, there are dp[i-1] ways to get to current node
            if int(one)<10 and int(one)>0:
                dp[i]+=dp[i-1]
                
            # if character at i and i-1 could convert to a letters, then there are another dp[i-2] ways to get here.
            if int(two)>9 and int(two)<27:
                dp[i] += dp[i-2]  if i >=2 else 1;
            
        return dp[len(s)-1]
        
