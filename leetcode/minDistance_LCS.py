class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # find the longest matched substring between word1 and word2
        # l1,l2 = 0 ,0
        # table = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]  # col : word1 , row : word2
        # mx = 0
        # for i in range(1,len(word2)+1):
        #     for j in range(1,len(word1)+1):
        #         if word2[i-1] == word1[j-1]:
        #             table[i][j] = table[i-1][j-1] + 1
        #             mx = max(mx,table[i][j])
        # print(mx,table)
        # return len(word1) + len(word2) - mx*2
        
        # find the longest matched subsequence between word1 and word2
        # example "park" "spake"  common subsequence is "pak". so answer is 3
        l1,l2 = 0 ,0
        table = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]  # col : word1 , row : word2
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else :
                    table[i][j] = max(table[i-1][j],table[i][j-1])
        # print(table)
        return len(word1) + len(word2) - table[len(word2)][len(word1)]*2

# "sea"
# "eat"
# "sea"
# "east"
# "leetcode"
# "etco"
# "t"
# "p"
# "t"
# "t"
# "park"
# "spake"