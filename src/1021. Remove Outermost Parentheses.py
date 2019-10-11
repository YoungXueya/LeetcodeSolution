class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res=[]
        left=0
        count=0
        for i in range(len(S)):
            if S[i]=='(':
                count+=1
            if S[i]==')':
                count-=1
            # print(count)
            #If Valid, return the inner one
            if count==0:
                # print(left+1,i)
                res+=[x for x in S[left+1:i]]
                # print(res)
                left=i+1
        return "".join(res)
            
        
