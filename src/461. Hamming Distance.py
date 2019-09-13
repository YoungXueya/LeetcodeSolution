class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #bin(): Convert an integer number to a binary string prefixed with “0b”. 
        result=bin(x^y).count('1')
       
        return result
    # x&(x-1) remove the last 1 in the number
    # It could also used to judge is a number is even:
    # if( (x&(x-1)) == 0 ) return 1;
    # else return 0;
    def hammingDistance(self, x: int, y: int) -> int:
        x=x^y
        count=0
        while x:
            x=x&(x-1)
            count+=1
        return count
    
        
