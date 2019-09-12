class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        setJ=set()
        for j in J:
            setJ.add(j)
        count=0
        for s in S:
            if s in setJ:
                count+=1
        return count
            
        
