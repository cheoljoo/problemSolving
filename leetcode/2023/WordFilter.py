class WordFilter:
    
    def __init__(self, words: List[str]):
        self.tprefix = {}
        self.tsuffix = {}
        self.mem = {}
        for i in range(len(words)):
            for l in range(len(words[i])):
                if words[i][0:l+1] not in self.tprefix:
                    self.tprefix[words[i][0:l+1]] = []
                self.tprefix[words[i][0:l+1]].append(i)
                if words[i][len(words[i])-(l+1):] not in self.tsuffix:
                    self.tsuffix[words[i][len(words[i])-(l+1):]] = []
                self.tsuffix[words[i][len(words[i])-(l+1):]].append(i)
        # for p in self.tprefix:
        #     print("tprefix:" , p , self.tprefix[p])
        # for p in self.tsuffix:
        #     print("tsuffix:" , p , self.tsuffix[p])
    def f(self, prefix: str, suffix: str) -> int:
        if (prefix,suffix) in self.mem:
            return self.mem[(prefix,suffix)]
        # print(prefix,suffix)
        if prefix not in self.tprefix or len(self.tprefix[prefix]) == 0:
            return -1
        if suffix not in self.tsuffix or len(self.tsuffix[suffix]) == 0:
            return -1
        # print(prefix,suffix,self.tprefix[prefix],self.tsuffix[suffix])
        ans = []
        pc = 0
        sc = 0
        while pc < len(self.tprefix[prefix]) and sc < len(self.tsuffix[suffix]):
            # print(pc,sc,self.tprefix[prefix][pc] , self.tsuffix[suffix][sc])
            if self.tprefix[prefix][pc] == self.tsuffix[suffix][sc]:
                ans.append(self.tprefix[prefix][pc])
                sc += 1
                pc += 1
            elif self.tprefix[prefix][pc] < self.tsuffix[suffix][sc]:
                pc += 1
            else :
                sc += 1
        # print("ans:",ans)
        if len(ans) == 0:
            self.mem[(prefix,suffix)] = -1
            return -1
        t = max(ans)
        self.mem[(prefix,suffix)] = t
        return t

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)