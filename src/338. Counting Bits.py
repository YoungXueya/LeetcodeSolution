class Solution:
    # 0: 0
    # 1: 1
    
    # 2(0+2): 10
    # 3(1+2): 11
    
    # 4(0+4): 100
    # 5(1+4): 101
    # 6(2+4): 110
    # 7(3+4): 111
   
    # 8(0+8): 1000
    # 9(1+8): 1001
    
    def countBits(self, num: int) -> List[int]:
        result=[0 for i in range(num+1)]
        offset=1
        for i in range(1,num+1):
            if offset*2==i:
                offset*=2
            result[i]=result[i-offset]+1
        return result
