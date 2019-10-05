class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        cache=0
        result=""
        while i>-1 or j>-1:
            temp=0
            if i>-1:
                temp+=ord(a[i])-ord('0')
                i-=1
            if j>-1:
                temp+=ord(b[j])-ord('0')
                j-=1
            temp+=cache
            result+=str(temp%2)
            # print(result)
            cache=temp//2
        if cache==1:
            result+=str(cache)
        # print(result.reverse())
        return result[::-1]
        
    def addBinary2(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        cache=0
        result=[]
        while i>-1 or j>-1:
            temp=0
            if i>-1:
                temp+=ord(a[i])-ord('0')
                i-=1
            if j>-1:
                temp+=ord(b[j])-ord('0')
                j-=1
            temp+=cache
            result.append(temp%2)
            # print(result)
            cache=temp//2
        if cache==1:
            result.append(1)
        # print(result.reverse())
        return "".join([str(x) for x in result[::-1]])
