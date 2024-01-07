class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        return self.bfs(0,0,triangle[0][0],triangle)
    
    def bfs(self,l,s,sm,triangle):
        t = math.inf
        for l in range(1,len(triangle)):
            for i in range(l+1):
                if i == 0:
                    triangle[l][i] += triangle[l-1][0]
                elif i == l:
                    triangle[l][i] += triangle[l-1][i-1]
                else :
                    triangle[l][i] += min(triangle[l-1][i-1],triangle[l-1][i])
                if l == len(triangle)-1:
                    t = min(t,triangle[l][i])
        return t