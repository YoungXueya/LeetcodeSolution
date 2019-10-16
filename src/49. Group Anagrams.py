import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for w in strs:
            key=tuple(sorted(w))
            if key in dic:
                dic[key].append(w)
            else:
                dic[key]=[w]
        
        return dic.values()
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        res=[]
        for i in range(len(strs)):
            counter=[0]*26
            for char in strs[i]:
                counter[ord(char)-ord('a')]+=1
            counter=tuple(counter)
            if counter in dic:
                dic[counter].append(strs[i])
            else:
                dic[counter]=[strs[i]]
        for item in dic:
            res.append(dic[item])
        return res
    
