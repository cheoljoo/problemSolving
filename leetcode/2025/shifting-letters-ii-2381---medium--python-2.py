# Runtime 60 ms Beats 58.18% /  Memory 41.24 MB Beats 86.06%

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pins = [0] * (len(s) + 1)
        sl = list(s)
        for start,end,dir in shifts:
            if dir == 1:  # forward : +1
                pins[start] += 1
                pins[end+1] -= 1
            else: # backward : -1
                pins[start] -= 1
                pins[end+1] += 1
        # print('pins',pins)
        shift = 0
        size = ord('z') - ord('a') + 1  # 26
        for i in range(len(s)):
            if pins[i] != 0:
                shift += pins[i]
            curPos = ord(sl[i]) - ord('a')
            gap = (curPos + shift) % size
            # print('i',i,'shift',shift,'sl[i]',sl[i],'curPos',curPos,'gap',gap,size)
            sl[i] = chr(ord('a')+gap)
        return ''.join(sl)