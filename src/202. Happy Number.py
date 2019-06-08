class Solution:
    def isHappy(self, n: int) -> bool:
        history=set()
        while n not in history:
            
            history.add(n)
            res=0
            while n!=0:
                cur=n%10
                n=int(n/10)
                res+=cur**2
            if res==1:
                return True
            n=res
        return False
