class queue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list1=[]
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.list1.insert(0,x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.list1.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.list1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.list1
        


#Your MyQueue object will be instantiated and called as such:
obj = queue()
obj.push(4)
obj.push(-1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)