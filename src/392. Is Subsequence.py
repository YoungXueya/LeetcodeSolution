class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counts=0
        countt=0
        while counts<len(s) and countt<len(t):
            if s[counts]==t[countt]:
                counts+=1
                countt+=1
            else:
                countt+=1
        print(counts)
        if counts==len(s):
            return True
        else:
            return False
