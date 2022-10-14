import bisect

class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = []
        bisect.insort(self.db[key] , (timestamp,value))
        # self.db[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""
        i = bisect.bisect_left(self.db[key],(timestamp,""))
        # print(i)
        if i < 0 :
            return ""
        elif i == 0:
            t,v = self.db[key][i]
            if timestamp < t:
                return ""
            return v
        elif i == len(self.db[key]):
            t,v = self.db[key][-1]
            if timestamp < t:
                return ""
            return v
        else :
            t,v = self.db[key][i]
            # print(key,i,timestamp,t,v,self.db[key])
            if timestamp < t:
                t,v = self.db[key][i-1]
                return v
            return v
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)