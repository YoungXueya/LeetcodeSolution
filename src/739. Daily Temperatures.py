class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result=[0 for i in range(len(T))]
        count=0
        for i in range(len(T)-2,-1,-1):
            if T[i]<T[i+1]:
                result[i]=1
            else:
                for j in range(i+result[i+1],len(T)):
                    if T[i]<T[j]:
                        result[i]=j-i
                        break
                    if result[j]==0:
                        break              
        return result
        
