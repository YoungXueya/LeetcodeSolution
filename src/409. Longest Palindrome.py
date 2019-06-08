class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping={}
        for i in range(len(s)):
            if s[i] in mapping:
                mapping[s[i]]+=1
            else:
                mapping[s[i]]=1
        odd=False
        count=0
        for item in mapping.keys():
            if mapping[item]%2!=0:
                odd=True
            if mapping[item]>=2:
                count+=int(mapping[item]/2)*2
        if odd:
            return count+1
        else:
            return count
