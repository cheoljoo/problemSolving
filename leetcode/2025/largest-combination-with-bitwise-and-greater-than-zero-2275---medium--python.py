class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # 각수가 가지는 bit를 계산한다.
        # 각 bit 자리수가 1인 숫자들의 갯수를 센다.
        # 이 수가 가장 큰 것을 답으로 하면 된다.
        self.sb = {}
        for candidate in candidates:
            self.setBit(candidate)
        ans = 0
        for sb in self.sb.values():
            if sb > ans:
                ans = sb
        return ans
    def setBit(self,c):
        sb = 1
        while c:
            if c % 2 == 1 :
                if sb not in self.sb:
                    self.sb[sb] = 0
                self.sb[sb] += 1
            c //= 2
            sb *= 2