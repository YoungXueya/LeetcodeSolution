class Solution:
    # It's quite confusing about the last word.
    # But the answer seems doesn't take the last ' ' as a sperate.
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=len(s)-1
        while i >=0:
            print(s[i])
            if(s[i]!=' '):
                
                i-=1
            else:
                break
        return len(s)-1-i
        
    def lengthOfLastWord1(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
