class Solution:
    # Saves more time!
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result=[[0 for i in range(j+1)] for j in range(len(triangle))]
        for level in range(len(triangle)-1,-1,-1):
            for i in range(level+1):
                #print(triangle[level][i])
                if level==len(triangle)-1:
                    result[level][i]=triangle[level][i]
                else:
                    result[level][i]=min(result[level+1][i],result[level+1][i+1])+triangle[level][i]
                #print(result[level][i])
        return result[0][0]
    
    # Easier to understand!
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        result=[[0 for i in range(j+1)] for j in range(len(triangle))]
        #print(result)
        def minRoute(level,index):
            if result[level][index]!=0:
                return result[level][index]
            if level==len(triangle)-1:
                res=triangle[level][index]
            else:
                res=triangle[level][index]+min(minRoute(level+1,index),minRoute(level+1,index+1))
            result[level][index]=res
            return res
                
        minRoute(0,0)
        return result[0][0]
        
