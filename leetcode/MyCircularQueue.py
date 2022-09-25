class MyCircularQueue:
    
    def __init__(self, k: int):
        self.size = k
        self.q = []

    def enQueue(self, value: int) -> bool:
        if self.isFull() == True:
            return False
        self.q.append(value)
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty() == True:
            return False
        self.q.pop(0)
        return True
        

    def Front(self) -> int:
        if not self.q:
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if not self.q:
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        if self.q:
            return False
        return True
        

    def isFull(self) -> bool:
        if len(self.q) == self.size:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()