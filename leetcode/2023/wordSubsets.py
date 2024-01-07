class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dwords2 = {}
        dwords1 = []
        ans = []
        for w in words2:
            tmpd = {}
            for ch in w:
                if ch not in tmpd:
                    tmpd[ch] = 0
                tmpd[ch] += 1
            for ch in tmpd:
                if ch not in dwords2:
                    dwords2[ch] = 0
                dwords2[ch] = max(dwords2[ch],tmpd[ch])
        for word1 in words1:
            tmpd = {}
            for ch in word1:
                if ch not in tmpd:
                    tmpd[ch] = 0
                tmpd[ch] += 1
            dwords1.append(tmpd)
        for i,t in enumerate(dwords1):
            fail = False
            for ch in dwords2:
                if ch not in t:
                    fail = True
                    break
                elif t[ch] < dwords2[ch]:
                    fail = True
                    break
            if not fail :
                ans.append(words1[i])
        return ans


# we need count of multple characters
# ["amazon","apple","facebook","gopogle","leetcode"]
# ["e","oo"]
# => ["facebook","gopogle"]
