import collections
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=collections.deque()
        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i].split('-')[-1].isdigit():
                stack.append(int(tokens[i]))
            else:
                # print(tokens[i])
                second=stack.pop()
                first=stack.pop()
                if tokens[i]=='+':
                    stack.append(first+second)
                elif tokens[i]=='-':
                    stack.append(first-second)
                elif tokens[i]=='*':
                    stack.append(first*second)
                else:
                    stack.append(int(float(first)/second))
                # print(stack[-1])
        return stack[0]
