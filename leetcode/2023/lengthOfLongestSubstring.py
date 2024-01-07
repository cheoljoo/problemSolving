class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # print(s)
        if not s :
            return 0
        pos = {}
        ls = set()  # longest string
        ans = 0 
        start = 0
        end = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in ls:
                p = pos.get(ch,0)
                for j in range(start,p):
                    ls.remove(s[j])
                start = p + 1
            else :
                ls.add(ch)
            end = i
            pos[ch] = i
            ans = max(ans,end - start +1)
            # print(start,end,ls)
        return ans

    
# "abcabcbb"
# "bbb"
# ""
# "p"
# "pwwkew"