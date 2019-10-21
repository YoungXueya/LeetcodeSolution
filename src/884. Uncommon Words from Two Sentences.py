class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dic={}
        res=[]
        for word in A.split():
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=-1
        for word in B.split():
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=-1
        for item in dic:
            if dic[item]<0:
                res.append(item)
        return res
        
