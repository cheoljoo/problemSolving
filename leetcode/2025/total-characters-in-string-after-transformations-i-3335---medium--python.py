# 3335. Total Characters in String After Transformations I : Runtime 5523 ms Beats 28.88%
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        d = [0] * 26
        for ch in s:
            d[ord(ch)-ord('a')] += 1
        # print(d)
        for i in range(t):
            tgt = [0] * 26
            for alpha in range(25):
                if d[alpha] != 0:
                    tgt[alpha+1] += d[alpha] % (10**9+7)
            if d[25] != 0:
                tgt[0] += d[25] % (10**9+7)
                tgt[1] += d[25] % (10**9+7)
            d = tgt
        ans = 0
        # print(d)
        for i in range(26):
            ans += d[i] % (10**9+7)
        return ans % (10**9+7)