class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1 :
            return [[1]]
        ans = []
        for i in range(n):
            r = [0 for _ in range(n)]
            ans.append(r)
        # right : 0
        # down : 1
        # left : 2
        # up : 3
        direction = 0
        r = 0  # row 
        c = 0  # column
        for i in range(n**2):
            ans[r][c] = i+1
            if direction == 0 :
                if c+1 >= n or ans[r][c+1] != 0 :
                    direction = 1
                    r = r+1
                else :
                    c = c+1
            elif direction == 1:
                if r+1 >=n or ans[r+1][c] != 0:
                    direction =2
                    c = c-1
                else :
                    r = r+1
            elif direction == 2:
                if c-1 < 0 or ans[r][c-1] != 0:
                    direction = 3
                    r = r-1
                else :
                    c = c-1
            else : # direction == 3
                if r-1 < 0 or ans[r-1][c] != 0:
                    direction = 0
                    c = c+1
                else :
                    r = r-1
                    
        return ans
            