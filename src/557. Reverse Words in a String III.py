class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.split(" ")
        res=[x[::-1] for x in res]
        return " ".join(res)
        
