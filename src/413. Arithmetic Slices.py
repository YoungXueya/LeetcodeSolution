class Solution:

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        cur=0
        result=0
        # That is that when
        # [1,2,3]: 1
        # [1,2,3,4]: [2,3,4][1,2,3,4] 2
        # [1,2,3,4,5]: [3,4,5][2,3,4,5][1,2,3,4,5] 3
        for i in range(2,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                cur+=1
                result+=cur
            else:
                cur=0
        return result
