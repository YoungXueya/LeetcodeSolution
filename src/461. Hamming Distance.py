class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #bin(): Convert an integer number to a binary string prefixed with “0b”. 
        result=bin(x^y).count('1')
       
        return result
    
        
