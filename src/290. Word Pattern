class Solution:
    # Consider situation:
    # 1. Length of pattern and str is different
    # 2. "abba" and "dog dog dog dog"
    def wordPattern(self, pattern: str, str: str) -> bool:
        mapping={}
        list=str.split()
        if(len(pattern)!=len(list)):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if(list[i]==mapping[pattern[i]]):
                    continue
                else:
                    return False
            else:
                if list[i] in mapping.values():
                    return False
                mapping[pattern[i]]=list[i]
        return True
        
