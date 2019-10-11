import collections
class Solution:
    def decodeString(self, s: str) -> str:
        curNum=0
        curString=''    # for the already duplicated string
        stack=collections.deque()
        for i in range(len(s)):
            if s[i].isdigit():
                curNum=curNum*10+int(s[i])
            elif s[i]=='[':
                stack.append(curString)
                stack.append(curNum)
                curString=''
                curNum=0
            elif s[i]==']':
                num=stack.pop()
                prevString=stack.pop()
                curString=prevString+curString*int(num)
            else:
                curString+=s[i]
        return curString
                
                       
        
