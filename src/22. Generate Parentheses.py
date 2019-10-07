class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.backTrack(res,"",0,0,n)
        return res
    
    def backTrack(self,res,str,open,close,max):
        if len(str)==max*2:
            res.append(str)
            return
        if (open<max):
            self.backTrack(res,str+'(',open+1,close,max)
        if (close<open):
            self.backTrack(res,str+')',open,close+1,max)
    
