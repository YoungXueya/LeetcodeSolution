class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        left=0
        res=[]
        for i in range(len(s)//(2*k)+1):
            res.append(s[left:min(left+k,len(s))][::-1])
            res.append(s[min(left+k,len(s)):min(left+2*k,len(s))])
            left+=2*k
        return "".join(res)
