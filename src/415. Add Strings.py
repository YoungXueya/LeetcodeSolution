class Solution:
    #
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        res=[]
        i,j=len(num1)-1,len(num2)-1
        
        while i>=0 or j>=0:
            n1 = ord(num1[i])-ord('0') if i>=0 else 0
            n2 = ord(num2[j])-ord('0') if j>=0 else 0
            i-=1
            j-=1
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
        
    # Cheating solution, because python has no limits
    def addStrings(self, num1: str, num2: str) -> str:
        val1=0
        val2=0
        for i in num1:
            val1=val1*10+(ord(i)-ord('0'))
            
        for j in num2:
            val2=val2*10+(ord(j)-ord('0'))
        return str(val1+val2)
            
                
