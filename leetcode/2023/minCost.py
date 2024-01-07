class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        old = colors[0]
        oldIndex = 0
        if len(colors) <= 1:
            return 0
        mx = neededTime[0]
        ans = 0
        removeSum = mx
        # print("=====",colors,neededTime)
        for i in range(1,len(colors)):
            if old == colors[i]:
                mx = max(mx,neededTime[i])
                removeSum += neededTime[i]
            else :
                old = colors[i]
                ans += removeSum - mx
                removeSum = neededTime[i]
                mx = neededTime[i]
            # print(colors[i],ans)
        ans += removeSum - mx
        return ans
                
        