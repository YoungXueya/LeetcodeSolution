class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2+1):
            if i==0 or len(s)%i!=0:
                continue
            j=i
            while j<len(s):
                # print(i,j,s[0:i],s[j:j+i])
                if s[0:i]==s[j:j+i]:
                    j+=len(s[0:i])
                    # print(j)
                else:
                    break
            if j>=len(s):
                return True
        return False
                
        
