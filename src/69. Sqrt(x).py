class Solution:
    # Binary Search 
    # Search range(1,x/2) when x>1.
    # Binary Seach judge requirment: left <=right
    def mySqrt(self, x: int) -> int:
        if x <=1:
            return x
        left=1
        right=int(x/2)
        mid=int((left+right)/2)
        while left<=right:
            print(mid)
            if mid**2>x:
                right=mid-1
            else:
                if (mid+1)**2>x:
                    return mid
                left=mid+1
            mid=int((left+right)/2)            
           
        return left+1
            
        
        
    
    def mySqrt1(self, x: int) -> int:
        return int(math.sqrt( x ))
