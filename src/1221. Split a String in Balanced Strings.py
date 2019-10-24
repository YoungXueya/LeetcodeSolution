class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L=0
        R=0
        count=0
        for i in range(len(s)):
            if s[i]=='L':
                L+=1
            else:
                R+=1  
            if L==R:
                count+=1
        return count
                
        
