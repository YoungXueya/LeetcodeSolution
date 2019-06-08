class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime=[True]*n
        count=0
        for i in range(2,n):
            if i*i>n:
                break
            else:
                for j in range(i*i,n,i):
                    isPrime[j]=False
        
        for i in range(2,n):
            if isPrime[i]==True:
                count+=1
        return count
                            
        
