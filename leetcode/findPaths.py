class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # DP
        # we calculate each move count for each node.
        self.m = m
        self.n = n
        self.dp = {}
        if maxMove == 0:
            return 0
        for i in range(1,maxMove+1):
            self.dp[i] = {}
        for mi in range(m):
            for ni in range(n):
                cnt = 0
                if mi-1 < 0:
                    cnt += 1
                if mi+1 >= m:
                    cnt += 1
                if ni-1 < 0 :
                    cnt += 1
                if ni+1 >= n:
                    cnt += 1
                self.dp[1][(mi,ni)] = cnt
        # print(self.dp)
        self.ans = 0
        r = startRow
        c = startColumn
        for mM in range(1,maxMove+1):
            self.ans += self.get(mM,r,c)
        return self.ans % (10**9+7)
    def get(self,mM,r,c):
        if (r,c) in self.dp[mM]:
            return self.dp[mM][(r,c)]
        cnt = 0
        if r-1 >= 0:
            cnt += self.get(mM-1,r-1,c)
        if r+1 < self.m:
            cnt += self.get(mM-1,r+1,c)
        if c-1 >= 0:
            cnt += self.get(mM-1,r,c-1)
        if c+1 < self.n:
            cnt += self.get(mM-1,r,c+1)
        self.dp[mM][(r,c)] = cnt
        return cnt

# 2
# 2
# 2
# 0
# 0
# 1
# 3
# 3
# 0
# 1
# 3
# 3
# 3
# 1
# 1
# 10
# 10
# 0
# 5
# 5