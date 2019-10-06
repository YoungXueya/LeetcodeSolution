class Solution:
    def convertToBase7(self, num: int) -> str:
        res=[]
        Flag=True if num<0 else False
        num=abs(num)
        if num==0:
            return '0'
        while(num!=0):
            res.append(num%7)
            num=num//7
        res="".join(str(x) for x in res[::-1])
        return '-'+res if Flag else res
