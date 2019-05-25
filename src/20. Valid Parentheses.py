# Use a stack to check 
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
                
            elif len(stack)==0 and (s[i]==')' or s[i]==']' or s[i]=='}') :
                return False
            elif s[i]==')' and stack.pop()=='(':
                continue
            elif s[i]==']' and stack.pop()=='[':
                continue
            elif s[i]=='}' and stack.pop()=='{':
                continue
            else:
                return False
        
        if len(stack)==0:
            return True
        else:
            return False
            
            
