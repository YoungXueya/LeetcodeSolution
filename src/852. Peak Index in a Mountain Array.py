class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i=0
        while i<len(A)-1:
            if A[i]<A[i+1]:
                i+=1
            else:
                return i
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left=0
        right=len(A)-1
        while(left<right):
            mid=int((left+right)/2)
            print(mid)
            if A[mid]<A[mid+1]:
                left=mid+1
            elif A[mid]>A[mid+1]:
                right=mid
        
        return left
                
    
