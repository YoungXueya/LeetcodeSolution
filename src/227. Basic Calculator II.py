class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        number=0
        stack=[]
        sign='+'
        for i in range(len(s)):
            if s[i].isdigit():
                number=number*10+int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i==(len(s)-1):
                
                if sign=='+':
                    stack.append(number)
                elif sign=='-':
                    stack.append(-number)
                elif sign=='*':
                    stack.append(stack.pop()*number)
                elif sign=='/':
                    first=stack.pop()
                    stack.append(first/number if first>0 else -(-first/number))
                
                # print(stack)
                sign=s[i]
                number=0
        print(stack)
        for n in stack:
            res+=n
        return res
            
