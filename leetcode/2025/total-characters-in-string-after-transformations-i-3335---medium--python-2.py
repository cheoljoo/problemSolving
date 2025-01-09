# 3335. Total Characters in String After Transformations I : Runtime 294 ms Beats 95.31%
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dq = deque()
        c = Counter(s)
        a = ord('a')
 
        for i in range(26):
            dq.append(c[chr(a + i)])
 
        for i in range(t):
            dq.rotate()
            dq[1] += dq[0]
 
        return sum(dq) % (10 ** 9 + 7)