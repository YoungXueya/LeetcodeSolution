class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(comb,index,remain):
            if remain==0 and len(comb)==k:
                if comb not in res:
                    res.append(comb)
                return 
            for i in range(index,10):
                if i>remain:
                    break
                else:
                    
                    dfs(comb+[i],i+1,remain-i)
        res=[]
        dfs([],1,n)
        return res
        
