class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(comb,index,remain):
            # print(index,comb)
            if remain==0:
                comb=sorted(comb)
                if comb not in res:
                    res.append(comb)
                return 
            for i in range(index,len(candidates)):
                if candidates[i]>remain:
                    break
                else:
                    # print("explore")
                    dfs(comb+[candidates[i]],i+1,remain-candidates[i])
        candidates=sorted(candidates)
        dfs([],0,target)
        return res
        
