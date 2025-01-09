# 2275. Largest Combination With Bitwise AND Greater Than Zero : Runtime 566 ms Beats 55.31%
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # bitwise and 과정에서 0이 되지 않는 가장 많은 수는 공통으로 1인 비트의 가장 많은 수와 같다.
        cnt = defaultdict(int)
 
        for v in candidates:
            i = 0
            while v:
                if v % 2:
                    cnt[i] += 1
                v = v // 2
                i += 1
 
        return max(cnt.values())