class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        
        def dfs(combination,remain,index):
            
            # print(combination)
            if remain==0:
                res.append(combination)
                return 
            for i in range(index,len(candidates)):
                if candidates[i]>remain:
                    break
                else:
                    dfs(combination+[candidates[i]],remain-candidates[i],i)
        candidates=sorted(candidates)
        # print(candidates)
        combination=[]
        dfs(combination,target,0)
        return res
        
