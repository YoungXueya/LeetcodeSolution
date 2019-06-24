class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i in range(len(shortest)):
            for item in strs:
                if(item[i]!=shortest[i]):
                    return shortest[:i]
        return shortest
        
        
