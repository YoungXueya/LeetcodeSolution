class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        stack=[]
        Len=0
        for i in range(len(S)):
            if S[i].isdigit():
                Len*=int(S[i])
            else:
                Len+=1
            stack.append(S[i])
            # print(Len,stack)
            while Len>=K:
                print(stack)
                while stack[-1].isdigit():
                    Len=Len//int(stack.pop())
                K%=Len
                # print(K)
                if K==0:
                    return stack[-1]
                stack.pop()
                Len-=1
                
                
                
        
