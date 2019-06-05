class Solution:
    # Judge whether a list can be partition into 3 equal sum part
    # Check the Array with S,2S,3S.
    # If the total sum cann't be divided by 3, it's definitely false.
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total=sum(A)
        if total %3!=0:
            return False
        part=0
        cnt=0
        for a in A:
            part=part+a
            if part!=int(total/3): 
                continue
            else: 
                cnt+=1
            if(cnt==3):
                return True
            part=0
        return False
            
