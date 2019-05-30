class Solution:
    def countAndSay(self, n: int) -> str:
        s=str(1)
        if(n==1):
            return str(1)
        
        for i in range(n-1):
            cur=s[0]
            count=1
            res=""
            for j in range(1,len(s)):
                if(s[j]==cur):
                    count+=1
                else:
                    res=res+str(count)+str(cur)
                    cur=s[j]
                    count=1
            res=res+str(count)+str(cur)
            s=res
        return s
                    
            
        
