class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if not num else 1+(num-1) % 9 
        
    def addDigits(self, num: int) -> int:
        while num>=10:
            tem=0
            while num!=0:
                tem+=num%10
                num//=10
            num=tem
        return num
