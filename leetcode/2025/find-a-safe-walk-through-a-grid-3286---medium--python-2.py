# 3286. Find a Safe Walk Through a Grid : Runtime 45 ms Beats 98.63%
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        d = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(grid)
        n = len(grid[0])
        visited = [ [0 for _ in range(n)] for _ in range(m) ]
        hq = []
 
        visited[0][0] = 1
        if grid[0][0]:
            health -= 1
 
        heapq.heappush(hq, (-health, 0, 0))
 
        while hq:
            h, i, j = heapq.heappop(hq)
            h = -h
            # print(f'i = {i}, j = {j}, h = {h}')
 
            if i == m - 1 and j == n - 1:
                return True
 
            for di, dj in d:
                ni = i + di
                nj = j + dj
                nh = h
                if not (0 <= ni < m) or not (0 <= nj < n) or visited[ni][nj] == 1:
                    continue
                if grid[ni][nj]:
                    nh -= 1
                if nh < 1:
                    continue
                visited[ni][nj] = 1
                # print(f'ni = {ni}, nj = {nj}, nh = {nh}')
                heapq.heappush(hq, (-nh, ni, nj))
 
        return False