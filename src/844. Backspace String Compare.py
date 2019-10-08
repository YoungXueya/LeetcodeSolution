class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.back(S)==self.back(T)
    
    def back(self,str):
        stack=[]
        for i in range(len(str)):
            if str[i]=='#':
                if stack:
                    stack.pop()
            else:
                stack.append(str[i])
        return stack
                
        
