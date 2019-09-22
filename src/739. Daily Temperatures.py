class Solution:
    # https://leetcode.com/problems/daily-temperatures/discuss/121787/C%2B%2B-Clean-code-with-explanation%3A-O(n)-time-and-O(1)-space-(beats-99.13)
    # Logic is if T[i]<T[i+1], if result[i+1]>0 means that the following result[i+1] is smaller than T[i],
    # Therefore, compare with elements at least result[i] latter.
    # End condition of comparison is if result[j]==0, then no other element bigger than T[i] latter.
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
        
