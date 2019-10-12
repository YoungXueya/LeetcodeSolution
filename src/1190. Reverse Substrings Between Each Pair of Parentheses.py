import collections
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=['']
        for i in range(len(s)):
            if s[i]=='(':
                stack.append('')
            elif s[i]==')':
                add=stack.pop()[::-1]
                stack[-1]+=add
            else:
                stack[-1]+=s[i]
        return stack[-1]
                
                
        
