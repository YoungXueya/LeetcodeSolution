class Solution:
     def countSegments(self, s: str) -> int:        
        return len(s.split())

    def countSegments(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        count=0
        for i in range(1,len(s)):
            if s[i]==' ' and s[i-1]!=' ':
                count+=1
        return count+1
