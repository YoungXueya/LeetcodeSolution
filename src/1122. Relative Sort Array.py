class Solution:
    
    # Initial idea
    # In-space, but O(n^2) time complexity
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        slow=0
        for item in arr2:
            for j in range(len(arr1)):
                if arr1[j]==item:
                    arr1[j],arr1[slow]=arr1[slow],arr1[j]
                    slow+=1
      
        self.quicksort(arr1,slow,len(arr1)-1)
        return arr1
    
    def quicksort(self,arr,start,end):
        if start>end:
            return 
        key=arr[start]
        i = start
        j = end
        while i<j:
            while i<j and arr[j]>=key:
                j-=1
            while i<j and arr[i]<=key:
                i+=1
            arr[i],arr[j]=arr[j],arr[i]
            
        arr[start],arr[i]=arr[i],arr[start]
        self.quicksort(arr,start,i-1)
        self.quicksort(arr,i+1,end)
        
    ## Better Solution using count, O(n) time and space complexity and 
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        slow=0
        dic={}
        diff=[]
        for item in arr2:
            dic[item]=0
        
        for j in range(len(arr1)):
            if arr1[j] in dic:
                dic[arr1[j]]+=1
            else:
                diff.append(arr1[j])
        
        diff.sort()
        count=[]      
        for item in arr2:
            count+=[item]*dic[item]
        count+=diff
        return count
    
        
            
        
