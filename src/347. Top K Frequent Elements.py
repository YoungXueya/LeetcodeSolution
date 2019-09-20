class Solution:
    #Tricky
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=collections.Counter(nums)
        return [c[0] for c in count.most_common(k)]
    
    # Awkward    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        dic=sorted(dic,key=dic.get, reverse=True)
        result=[]
        index=0
        for item in dic:
            if index<k:
                index+=1
                result.append(item)
            else:
                break
        return result
