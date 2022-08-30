class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        nDigitCnt = self.digitCount(n)
        power = 0
        powerDigitCnt = 0
        self.powerLD = {}
        while powerDigitCnt <= nDigitCnt :
            powerDigitCnt = self.digitCount(2**power)
            if nDigitCnt == powerDigitCnt:
                self.powerAnalysis(2**power)
            power += 1
        # print("powerLD:",self.powerLD)
        nL = {}
        p = n
        while p :
            remain = p % 10
            if remain not in nL:
                nL[remain] = 0
            nL[remain] += 1
            p //= 10
        for _,ld in self.powerLD.items():
            if self.equal(ld ,nL) == True:
                return True
        return False
    def equal(self,ld,nL):
        flag = True
        for i,v in ld.items():
            if i not in nL or v != nL[i]:
                return False
        return flag
    def digitCount(self,n):
        cnt = 0
        while n :
            cnt += 1
            n //= 10
        return cnt
    def powerAnalysis(self,n):
        self.powerLD[n] = {}
        p = n
        while p :
            remain = p % 10
            if remain not in self.powerLD[n]:
                self.powerLD[n][remain] = 0
            self.powerLD[n][remain] += 1
            p //= 10
            
    