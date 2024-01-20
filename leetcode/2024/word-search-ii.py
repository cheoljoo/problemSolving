class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words.sort(reverse=True)
        # print(words)
        self.R = len(board)
        self.C = len(board[0])
        self.S = {}
        self.N = {} # neighbor  : set()
        self.matched = {}
        self.board = board
        for row in range(self.R):
            for col in range(self.C):
                ch = board[row][col]
                if ch not in self.S:
                    self.S[ch] = []
                self.S[ch].append( (row,col) )
                if ch not in self.N:
                    self.N[ch] = set()
                if row-1 >= 0:
                    self.N[ch].add(board[row-1][col])
                if row+1 < self.R :
                    self.N[ch].add(board[row+1][col])
                if col+1 < self.C:
                    self.N[ch].add(board[row][col+1])
                if col-1 >= 0:
                    self.N[ch].add(board[row][col-1])
        ans = []
        for word in words:
            org = word
            if word in self.matched:
                ans.append(word)
                continue
            direction = True
            firstchcnt = 0
            lastchcnt = 0
            if word[0] != word[-1]:
                for i in range(len(word)):
                    if word[i] == word[0]:
                        firstchcnt += 1
                    if word[i] == word[-1]:
                        lastchcnt += 1
                if lastchcnt > firstchcnt:
                    direction = False
            neighborFlag = True
            for i in range(len(word)-1):
                if word[i] not in self.S or word[i+1] not in self.S:
                    neighborFlag = False
                    break
                if word[i+1] not in self.N.get(word[i],set()):
                    neighborFlag = False
                    break
            if neighborFlag == False:
                continue
            if direction == False:
                word = ''.join(reversed(word))
                if word in self.matched:
                    ans.append(org)
            # print('direction',direction,word,org)
            start = word[0]
            if start in self.S:
                for row,col in self.S[start]:
                    self.go(1,word,row,col)
            if word in self.matched:
                ans.append(org)
                rword = ''.join(reversed(word))
                for i in range(len(rword)):
                    self.matched[rword[:i+1]] = 1 
            # print('!',word,org,self.matched,'ans',ans)
        return ans
    def go(self,idx,w,row,col):
        val = self.board[row][col]
        self.board[row][col] = '#'
        if idx >= len(w):
            self.matched[w] = 1 #copy.deepcopy(path)
            self.board[row][col] = val
            return
        else:
            self.matched[w[:idx]] = 1 #copy.deepcopy(path)
        # print(idx,w, 'm',list(self.matched.keys()),'p',path)
        t = w[idx]
        if col+1 < self.C and self.board[row][col+1] == t and self.board[row][col+1] != '#':
            self.go(idx+1,w,row,col+1)
        if col-1 >= 0 and self.board[row][col-1] == t and self.board[row][col-1] != '#':
            self.go(idx+1,w,row,col-1)
        if row+1 < self.R and self.board[row+1][col] == t and self.board[row+1][col] != '#':
            self.go(idx+1,w,row+1,col)
        if row-1 >= 0 and self.board[row-1][col] == t and self.board[row-1][col] != '#':
            self.go(idx+1,w,row-1,col)
        self.board[row][col] = val
        return