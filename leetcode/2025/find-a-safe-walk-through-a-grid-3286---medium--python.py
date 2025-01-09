class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # ohealth = health
        # R = len(grid)
        # C = len(grid[0])
        # rowSet = set()
        # for r in range(R):
        #     flag = True
        #     for c in range(C):
        #         if grid[r][c] == 0:
        #             flag = False
        #     if flag:
        #         rowSet.add(r)
        #         health -= 1
        # colSet = set()
        # for c in range(C):
        #     flag = True
        #     for r in range(R):
        #         if grid[r][c] == 0:
        #             flag = False
        #     if flag:
        #         colSet.add(c)
        #         health -= 1
        # # print('health',health,R+C-1,ohealth)
        # newGrid = []
        # for r in range(R):
        #     row = []
        #     if r not in rowSet:
        #         for c in range(C):
        #             if c not in colSet:
        #                 row.append(grid[r][c])
        #         newGrid.append(row)
        # grid = newGrid
        # if not grid:
        #     return R+C-1 < ohealth
        R = len(grid)
        C = len(grid[0])
        # self.printGrid(-100,-100,grid,R,C,-1,health)
        if health <= 0:
            return False
        ones = [ [-1] * C for _ in range(R) ]
        ones[0][0] = grid[0][0]
        hq = [(grid[0][0],0,0)]  # (oneCount,r,c)
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        while hq:
            oneCount,r,c = heapq.heappop(hq)
            grid[r][c] = -1
            # self.printGrid(r,c,grid,R,C,oneCount,health)
            # print('hq',hq)
            if oneCount >= health:
                return False
            if oneCount + R-1 - r + C-1 - c < health:
                # print('health',oneCount,R,r,C,c,oneCount+R-r+C-c-2,'h',health)
                return True
            if r == R-1 and c == C-1 and oneCount < health:
                # print('oneCount',r,R,c,C,oneCount , health)
                return True
            for dr,dc in direction:
                nr = r + dr
                nc = c + dc
                # print(nr,nc,grid[nr][nc],ones[nr][nc])
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1 and ones[nr][nc] < (oneCount + grid[nr][nc]):
                    ones[nr][nc] = oneCount + grid[nr][nc]
                    heapq.heappush(hq,(oneCount + grid[nr][nc] ,nr,nc))
        return False
    def printGrid(self,r,c,grid,R,C,one,h):
        print('GRID',r,c,'oneCount',one,'health',h)
        for ri in range(R):
            print(grid[ri])