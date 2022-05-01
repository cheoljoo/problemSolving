from bisect import bisect_left
from collections import deque

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
        elif self.arr[-1] <= num :
            self.arr.append(num)
        elif self.arr[0] >= num :
            self.arr.insert(0,num)
        else:
            idx = bisect_left(self.arr,num)
            self.arr.insert(idx,num)
        # print(self.arr)

    def findMedian(self) -> float:
        l = len(self.arr)
        if l%2 == 1:
            l //=2
            return 1.0*self.arr[l]
        else :
            l //= 2
            return 1.0*(self.arr[l-1]+self.arr[l])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()