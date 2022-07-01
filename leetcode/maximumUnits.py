class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1] ,reverse=True)
        # print(boxTypes)
        ans = 0
        for box,unit in boxTypes:
            if box <= truckSize:
                ans += box * unit
                truckSize -= box
            else:
                ans += truckSize * unit
                truckSize = 0
                break
        return ans