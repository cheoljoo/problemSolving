class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numLand = 0
        rx = len(grid)
        cx = len(grid[0])
        grp = [[0] * cx for _ in range(rx)]
        link = []
        # print(grp)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                flagLand = False
                if grid[r][c] != "1":
                    continue
                grp1 , grp2 = 0 , 0
                if r-1 >= 0 and grid[r-1][c] == "1":  # up
                    flagLand = True
                    grp1 = grp[r-1][c]
                # if r+1 < rx and grid[r+1][c] == "1":  # down
                #     flagLand = True
                if c-1 >= 0 and grid[r][c-1] == "1": #left
                    flagLand = True
                    grp2 = grp[r][c-1]
                # if c+1 < cx and grid[r][c+1] == "1": # right
                #     flagLand = True
                if flagLand == False:
                    numLand += 1
                    grp[r][c] = numLand
                else :
                    if grp1 != 0 and grp2 != 0 and grp1 != grp2:
                        grp[r][c] = grp1
                        link.append([grp1,grp2])
                    elif grp1 != 0:
                        grp[r][c] = grp1
                    elif grp2 != 0:
                        grp[r][c] = grp2
                # print("r:",r,"c:",c,"flagLand:",flagLand,"num:",numLand,grp,link)
        # print("r:",r,"c:",c,"flagLand:",flagLand,"num:",numLand,grp,link)
        # print("link:",link,"num:",numLand)
        # self.prt(grp)
        self.p = [ i for i in range(numLand+1)]
        for a,b in link:
            ap = self.parent(a)
            bp = self.parent(b)
            self.p[ap] = bp
            # print("link:",link,ap,bp)
        # print("p:",self.p)
        ans = {}
        for i in range(1,numLand+1):
            ans[self.parent(self.p[i])]=1
        # print("ans:",ans)
        return len(ans)
    def parent(self,a):
        while self.p[a] != a:
            a = self.p[a]
        return a
    def prt(self,grp):
        for r in range(len(grp)):
            for c in range(len(grp[0])):
                print(grp[r][c],"",end="")
            print()