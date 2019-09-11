class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        index=len(A)-1
        carry=0
        while index>=0 and K:
            temp=0
            if K:
                temp+=K%10
                K=K//10
            # print(temp)
            if index>=0:
                temp+=A[index]
                # print("A",A[index])
            temp+=carry
            print(temp)
            carry,A[index]=divmod(temp,10)
            index-=1
        # K is bigger
        while K:
            temp=0
            temp+=K%10+carry
            K=K//10
            carry,value=divmod(temp,10)
            A.insert(0,value)
        A is bigger and there is a carry
        while index>=0 and carry:
            temp=0
            temp+=A[index]+carry
            carry,A[index]=divmod(temp,10)
            index-=1
        # There is still a carry
        if carry:
            A.insert(0,1)
        return A
            
        
      
