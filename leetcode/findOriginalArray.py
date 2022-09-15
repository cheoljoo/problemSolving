class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        while len(changed):
            v = changed.pop(0)
            ans.append(v)
            d = v*2
            idx = bisect_left(changed,d)
            if idx == len(changed) or changed[idx] != d:
                return []
            changed.pop(idx)
        return ans