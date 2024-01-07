class Solution:
    def prt(self,mat):
        print("----")
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                print(mat[r][c],"",end="")
            print()
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        v = []
        rx = len(mat)
        cx = len(mat[0])

        for idx in reversed(range(cx)):
            sri = 0 # start row index
            sci = idx
            sv = []
            while sci < cx and sri < rx:
                sv.append(mat[sri][sci])
                sri += 1
                sci += 1
            sv.sort()
            sri = 0 # start row index
            sci = idx
            while sci < cx and sri < rx :
                mat[sri][sci] = sv.pop(0)
                sri += 1
                sci += 1
        # self.prt(mat)
        for idx in range(1,rx):
            sri = idx
            sci = 0
            sv = []
            while sci < cx and sri < rx :
                sv.append(mat[sri][sci])
                sri += 1
                sci += 1
            sv.sort()
            sri = idx
            sci = 0
            while sci < cx and sri < rx :
                mat[sri][sci] = sv.pop(0)
                sri += 1
                sci += 1            
        # self.prt(mat)
        return mat