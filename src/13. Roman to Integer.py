class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        left=0
        right=0
        # Flag=True
        for i in range(len(s)-1):
            if dic[s[i]]>=dic[s[i+1]]:
                right+=dic[s[i]]
            else:
                left+=dic[s[i]]
        right+=dic[s[-1]]
        return right-left
            
