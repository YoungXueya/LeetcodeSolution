class Solution:
    # backtracking
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        if not digits:
            return res
        self.dfs(digits,dic,0,"",res)
        return res
        
    def dfs(self,digits,dic,index,path,res):
        if len(path)==len(digits):
            # print(len(digits),digits,len(path),path)
            res.append(path)
            return 
        for j in dic[digits[index]]:
            self.dfs(digits,dic,index+1,path+j,res)
        
     # Iteractive,quicker
        
    def letterCombinations1(self, digits: str) -> List[str]:
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result=['']
        if not digits:
            return []
        for digit in digits:
            result=[p+q for p in result for q in dic[digit]]
        return result
            
            
        
