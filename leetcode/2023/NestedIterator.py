# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.n = nestedList
        self.stack = [[self.n,0]]
        self.cur = self.n
        # print("__init__:n",self.n)
    def next(self) -> int:
        # print("next:",self.curPos, self.cur)
        t = self.cur[self.curPos].getInteger()
        # print("next:",t)
        return t
    def hasNext(self) -> bool:
        if not self.stack:
            self.stack.append([self.n,0])
        # print("hasNext:n")    
        while self.stack:
            self.cur , self.curPos = self.stack[-1]
            # print("hasNext-2:", len(self.cur)  , self.curPos, self.cur)
            if self.curPos < len(self.cur) and self.cur[self.curPos].isInteger() == True:
                # print("True:cur" ,self.curPos, self.cur[self.curPos])
                self.stack[-1][1] += 1
                return True
            if self.curPos >= len(self.cur):
                p,pos = self.stack.pop()
                if self.stack:
                    self.stack[-1][1] += 1
                # print("pop:",pos, p)
            else:
                self.cur = self.cur[self.curPos].getList()
                # print("getList:cur",len(self.cur),self.cur)
                self.stack.append([self.cur,0])
                    
        # print("False")
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())