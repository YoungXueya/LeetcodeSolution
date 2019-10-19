class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        res=[]
        print(arr)
        diff=arr[len(arr)-1]-arr[0]
        print(diff)
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<diff:
                diff=arr[i+1]-arr[i]
                if res:
                    res.clear()
                res.append([arr[i],arr[i+1]])
            elif arr[i+1]-arr[i]==diff:
                res.append([arr[i],arr[i+1]])
        return res
        
