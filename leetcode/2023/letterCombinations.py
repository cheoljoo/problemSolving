class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.table = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']
                }
        # size = 1
        # for v in digits:
        #     size *= len(self.table[v])
        # ans = ["" for _ in range(size)]
        self.ans = []
        self.go("",0,digits)
        return self.ans
    def go(self,s,idxDigits,digits):
        if idxDigits >= len(digits):
            self.ans.append(s)
            return
        for ci,c in enumerate(self.table[digits[idxDigits]]):
            self.go(s+c,idxDigits+1,digits)
                
            