class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        maxIndex=[0 for i in range(26)]
        last=0
        start=0
        res=[]
        for i in range(len(S)):
            maxIndex[ord(S[i])-ord('a')]=i
        
        for i in range(len(S)):
            last=max(last,maxIndex[ord(S[i])-ord('a')])
            if last==i:
                res.append(last-start+1)
                start=last+1
        return res
