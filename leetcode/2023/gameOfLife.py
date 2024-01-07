class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nb = []
        rowC = len(board)
        colC = len(board[0])
        rowEmpty = [ 0 for _ in range(colC+2)]
        nb.append(rowEmpty)
        for i in range(rowC):
            nb.append([0] + board[i] + [0])
        nb.append(rowEmpty)
        # print(nb)
        for r in range(1,rowC+1):
            for c in range(1,colC+1):
                if nb[r][c] == 1:
                    p = sum(nb[r-1][c-1:c+2]) + sum(nb[r][c-1:c+2]) + sum(nb[r+1][c-1:c+2]) -1
                    if p ==2 or p == 3:
                        board[r-1][c-1] = 1
                    else :
                        board[r-1][c-1] = 0
                else :
                    p = sum(nb[r-1][c-1:c+2]) + sum(nb[r][c-1:c+2]) + sum(nb[r+1][c-1:c+2])
                    if p == 3 :
                        board[r-1][c-1] = 1
                    else :
                        board[r-1][c-1] = 0
                # print(nb[r][c],r,c,p)
        return 