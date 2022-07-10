class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1,100,1,1,1,100,1,1,100,1] + [0]
        # max(-1) = 0 = num[-1]
        # max(-2) = num[-2]
        # max(-3) = num[-3] + min( max(-2) , max(-1) )
        if len(cost) == 2:
            return min(cost)
        cost.append(0)
        dp = {}
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]
        for i in range(3,len(cost)+1):
            mi = -i
            dp[mi] = cost[mi] + min(dp[mi+1],dp[mi+2])
        return min(dp[-len(cost)],dp[-len(cost)+1])
            