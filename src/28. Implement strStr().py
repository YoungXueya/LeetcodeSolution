class Solution:
     def strStr1(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
        
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                j=1
                while  j<len(needle):
                    if haystack[i+j]!=needle[j]:
                        break
                    j+=1
                if(j==len(needle)):
                    return i
        return -1
            
    
                    
                    
