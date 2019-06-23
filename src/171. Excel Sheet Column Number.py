class Solution:
    def titleToNumber(self, s: str) -> int:
        res=0
        for i in range(0,len(s)):
            #print(ord(s[i])-ord('A'))
            res=res*26+ord(s[i])-ord('A')+1
        return res
        
