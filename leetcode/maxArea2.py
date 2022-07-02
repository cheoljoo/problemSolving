class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxH = 0
        old = 0
        for v in horizontalCuts:
            maxH = max(maxH,v-old)
            old = v
        maxH = max(maxH,h - old)
        maxV = 0
        old = 0
        for v in verticalCuts:
            maxV = max(maxV,v-old)
            old = v
        maxV = max(maxV,w - old)
        return ( maxH * maxV ) % (10**9 + 7)
        