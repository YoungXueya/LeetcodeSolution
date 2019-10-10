class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[]
        
        for i in range(len(S)):
            if S[i]=='(':
                stack.append(0)
            else:
                top=stack.pop()
                if top==0:
                    score=1
                else:
                    score=2*top
                stack[-1]+=score
                
        return stack[0]
        
