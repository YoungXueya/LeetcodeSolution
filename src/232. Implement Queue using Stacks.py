import collections
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first=collections.deque()   
        self.second=collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.first.append(x)
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for i in range(len(self.first)-1):
            self.second.append(self.first.pop())
        top=self.first.pop()
        for i in range(len(self.second)):
            self.first.append(self.second.pop())
        return top

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.first[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.first)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
