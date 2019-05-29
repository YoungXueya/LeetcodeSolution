class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        if len(s)<2:
            return s
        # consider both odd and even number of characters in a palindrome string
        # choose the longest one from history result and current odd and even 
        for i in range(len(s)):
            odd=self.search(s,i,i)
            even=self.search(s,i,i+1)
            res=max(res,odd,even,key=len)
        return res
    
    def search(self,s,left,right):
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        # Notice that slicing of a string doesn't include the end but the left.
        return s[left+1:right]
