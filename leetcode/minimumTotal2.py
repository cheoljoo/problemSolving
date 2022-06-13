class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        # ss,se = 0,0
        # for i in range(len(triangle)):
        #     ss += triangle[i][0]
        #     se += triangle[i][i]
        # self.mn = min(se,ss)
        self.bfs(0,0,triangle[0][0],triangle)
        return min(triangle[len(triangle)-1])
    def bfs(self,l,s,sm,triangle):
        for l in range(1,len(triangle)):
            for i in range(l+1):
                if i == 0:
                    triangle[l][i] += triangle[l-1][0]
                elif i == l:
                    triangle[l][i] += triangle[l-1][i-1]
                else :
                    triangle[l][i] += min(triangle[l-1][i-1],triangle[l-1][i])
        # if l == len(triangle)-1:
        #     self.mn = min(self.mn, sm)
        #     return
        # # if sm >= self.mn:
        # #     return 
        # self.dfs(l+1,s,sm+triangle[l+1][s],triangle)
        # self.dfs(l+1,s+1,sm+triangle[l+1][s+1],triangle)