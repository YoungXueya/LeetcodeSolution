class Solution:
    def myAtoi(self, str: str) -> int:
        res=[]
        Flag=False
        symbol="+"
        for i in range(len(str)):
            if str[i]==" ":
                if Flag:
                    break
                else:
                    continue
            else:
                if ord(str[i])-ord('0')>=0 and ord(str[i])-ord('0')<=9:
                    Flag=True
                    res.append(ord(str[i])-ord('0'))
                elif not Flag and (str[i]=='-' or str[i]=='+'):
                    
                    symbol=str[i]
                    Flag=True
                else:
                    break
        temp=0      
        for i in range(len(res)):
            temp=temp*10+res[i]
        if symbol=="+":
            return min(temp,2147483647)
        else:
            return max(0-temp,-2147483648)
            
