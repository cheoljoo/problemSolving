class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matLen = len(matrix)
        for i in range(matLen//2):
            sr , sc = i , i
            for diff in range(matLen-2*i-1):
                n = matrix[sr][sc+diff]
                l = matrix[sr+diff][matLen-1-sc]
                s = matrix[matLen-1-sr][matLen-1-sc-diff]
                w = matrix[matLen-1-sc-diff][sc]
                # print(" n:",sr,sc+diff,n,end="")
                # print(", l:",sr+diff,matLen-1-sc,l,end="")
                # print(", s:",matLen-1-sr,matLen-1-sc-diff,s,end="")
                # print(", w:",matLen-1-sc-diff,sc,w)
                matrix[sr+diff][matLen-1-sc] = n
                matrix[matLen-1-sr][matLen-1-sc-diff] = l
                matrix[matLen-1-sc-diff][sc] = s
                matrix[sr][sc+diff] = w
                # self.prt(matrix)
        return
    def prt(self,m):
        for r in range(len(m)):
            for c in range(len(m[0])):
                print(m[r][c],"",end="")
            print()
            