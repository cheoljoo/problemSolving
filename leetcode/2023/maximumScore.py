class Solution:
    def __init__(self):
        self.dp = {}
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.n = nums
        self.m = multipliers
        # print(len(nums),len(multipliers))
        return self.recur(0,len(self.n)-1,0)
        
    def recur(self,ns,ne,ms):
        if ms == len(self.m):
            return 0
        if (ns,ne,ms) in self.dp:
            return self.dp[(ns,ne,ms)]
        a = self.n[ns]
        b = self.n[ne]
        r = a * self.m[ms] + self.recur(ns+1,ne,ms+1)
        l = b * self.m[ms] + self.recur(ns,ne-1,ms+1)
        t = max(r,l)
        self.dp[(ns,ne,ms)] = t
        return t