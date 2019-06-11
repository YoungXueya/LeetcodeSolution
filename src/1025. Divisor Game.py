class Solution:
    # This is an interesting problem
    # First, if Alice lose N-1, then she can take 1 first and leave the lose situation(N-1) to Bob
    # So, lose N-1 will win N. 
    # Any odd number, only have odd number, it will only have even number after minus.
    # In this case, even number wins. Odd number will leave opponents an even number
    def divisorGame(self, N: int) -> bool:
        return N%2==0
