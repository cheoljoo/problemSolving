class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mem = {}
        for ch in s:
            if ch not in mem:
                mem[ch] = 0
            mem[ch] += 1
        for ch in t:
            if ch not in mem:
                return False
            if mem[ch] == 0:
                return False
            mem[ch] -= 1
        return True