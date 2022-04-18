class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 : column , text2 : row
        table = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        # table[1][1] = 1
        # table[2][3] = 2
        # print(table)
        for r in range(1,len(text2)+1):
            for c in range(1,len(text1)+1):
                if text1[c-1] == text2[r-1]:
                    table[r][c] = table[r-1][c-1] + 1
                else : # text1[c] != text2[r]:
                    table[r][c] = max(table[r-1][c],table[r][c-1])
        return table[len(text2)][len(text1)]