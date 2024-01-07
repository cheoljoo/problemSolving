class UndergroundSystem:

    def __init__(self):
        self.ckIn = {} # self.ckIn:id = [from,time]
        self.ckOut = {} # self.ckOut:(startStation,endStation) = [sum of time , sum of count] 

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.ckIn :
            if self.ckIn[id][1] != 0:
                print("error:" , id , self.ckIn[id][0] , self.ckIn[id][1])
                return
            else :
                self.ckIn[id][0] = stationName 
                self.ckIn[id][1] = t
        else :
            self.ckIn[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        f = self.ckIn[id][0]
        startTime = self.ckIn[id][1]
        self.ckIn[id][1] = 0
        if (f,stationName) in self.ckOut:
            self.ckOut[(f,stationName)][0] += t-startTime
            self.ckOut[(f,stationName)][1] += 1
        else:
            self.ckOut[(f,stationName)] = [t-startTime,1]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation,endStation) in self.ckOut:
            return self.ckOut[(startStation,endStation)][0] / self.ckOut[(startStation,endStation)][1]
        else :
            return 0.0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.self.ckIn(id,stationName,t)
# obj.self.ckOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)