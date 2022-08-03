class MyCalendar:
    
    def __init__(self):
        self.l = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.l:
            if s <= start and start < e:
                return False
            elif s <= end-1 and end-1 < e:
                return False
            elif start <= s and e <= end-1:
                return False
        self.l.append([start,end])
        return True
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)