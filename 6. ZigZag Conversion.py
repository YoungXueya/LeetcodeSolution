class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=1 or  numRows==1 or numRows>=len(s):
            return s
      
        res=[]
        for i in range(numRows):
            count=0
            temp=i
            while temp<len(s):
                temp=i+count*(numRows-1)*2
                if temp<len(s):
                    res.append(s[temp])
                if i!=0 and i !=numRows-1:
                    if temp+(numRows-1-i)*2<len(s):
                        res.append(s[temp+(numRows-1-i)*2])
                count+=1
                # print(i,temp,count,res)
        return "".join(res)
        
                    
