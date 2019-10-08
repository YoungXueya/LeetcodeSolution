class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res=[]
        i=0
        while i<len(A) and A[i]<0 :
            i+=1
        j=i-1
        # print(j)
        while i<len(A) and j>-1:
            if abs(A[i])<abs(A[j]):
                
                res.append(A[i]*A[i])
                i+=1
            else:
                res.append(A[j]*A[j])
                j-=1
        while j>-1:
            res.append(A[j]*A[j])
            j-=1
        while i<len(A):
            res.append(A[i]*A[i])
            i+=1
        return res
                
