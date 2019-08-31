class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p=[]
        
        

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin==None or x<curMin:
            curMin=x
        self.p.append((x,curMin))
        

    def pop(self) -> None:
        self.p.pop()
        

    def top(self) -> int:
        return self.p[-1][0]

    def getMin(self) -> int:
        if self.p:
            return self.p[-1][1]
        return sys.maxsize  


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
