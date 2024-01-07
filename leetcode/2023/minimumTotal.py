class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        ss,se = 0,0
        for i in range(len(triangle)):
            ss += triangle[i][0]
            se += triangle[i][i]
        self.mn = min(se,ss)
        self.dfs(0,0,triangle[0][0],triangle)
        return self.mn
    def dfs(self,l,s,sm,triangle):
        if l == len(triangle)-1:
            self.mn = min(self.mn, sm)
            return
        # if sm >= self.mn:
        #     return 
        self.dfs(l+1,s,sm+triangle[l+1][s],triangle)
        self.dfs(l+1,s+1,sm+triangle[l+1][s+1],triangle)