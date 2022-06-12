class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else :
                return s[0]
        # print(s)
        self.lmax = 0
        ans = (0,0)
        for i in range(1,len(s)):
            a,b = self.lpOdd(i,s)
            # print("odd  i:",i,self.lmax,b-a+1,a,b,s[a:b+1])
            if self.lmax < b-a+1:
                self.lmax = b-a+1
                ans = [a,b]
            a,b = self.lpEven(i,s)
            # print("even i:",i,self.lmax,b-a+1,a,b,s[a:b+1])
            if self.lmax < b-a+1:
                self.lmax = b-a+1
                ans = [a,b]
        return s[ans[0]:ans[1]+1]
    def lpOdd(self,idx:int,s:str):
        # if idx is center , odd
        size = min(idx , len(s)-1-idx)
        if self.lmax >= size*2+1:
            return (0,0)
        # print("odd  size:",size,"idx:",idx)
        for i in range(size):
            diff = i + 1
            if s[idx-diff] != s[idx+diff]:
                # print(idx-diff+1,idx+diff-1)
                return (idx-diff+1,idx+diff-1)
        return (idx-diff,idx+diff)
    def lpEven(self,idx:int,s:str):
        # if (idx-1) | (idx) is center , even
        size = min(idx , len(s)-idx)
        if self.lmax >= size*2:
            return (0,0)
        # print("even size:",size,"idx:",idx)
        for i in range(size):
            if s[idx-i-1] != s[idx+i]:
                # print(idx-i-1,idx+i)
                return (idx-i-1+1,idx+i-1)
        return (idx-size,idx+size-1)

# "abb"
# "b"
# "bb"
# "bc"
# "babad"
# "babab"
# "cbbd"
# "acbbct"
# "cbbabbc"