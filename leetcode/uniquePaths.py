class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n :
            m , n = n , m
        table = [[-1]*(n+1) for _ in range(m+1)]
        for r in range(m+1):
            table[r][n] = 0
        for c in range(n+1):
            table[m][c] = 0
        table[m-1][n-1] = 1   # init
        # n >= m 
        for c in reversed(range(n-1)):
            rr = m-1
            cc = c
            while True:
                # print(rr,cc)
                if rr < 0 or cc > n-1:
                    break
                table[rr][cc] = table[rr+1][cc] + table[rr][cc+1]
                rr -= 1
                cc += 1
                
        # print(table)
        for r in reversed(range(m-1)):
            rr = r
            cc = 0
            while True:
                if rr < 0 or cc > n-1:
                    break
                table[rr][cc] = table[rr+1][cc] + table[rr][cc+1]
                rr -= 1
                cc += 1
        # print(table)
        return table[0][0]