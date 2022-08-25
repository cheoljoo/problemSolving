class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for v in magazine:
            if v not in d:
                d[v] = 0
            d[v] += 1
        for v in ransomNote:
            if v not in d:
                return False
            if d[v] < 1 :
                return False
            d[v] -= 1
        return True