class Solution:
    def largestInteger(self, num: int) -> int:
        index = 0
        odd = []
        even = []
        eachIsEven = []
        n = num
        while True:
            r = n % 10
            if r % 2 == 0 :
                eachIsEven.append(1)
                even.append(r)
            else :
                eachIsEven.append(0)
                odd.append(r)
            # print(n)
            if n < 10:
                break
            n = n // 10
        # print(eachIsEven)
        even.sort()
        odd.sort()
        # print(even)
        # print(odd)
        ansList = []
        s = 0
        for v in reversed(eachIsEven):
            # print(v)
            if v == 1 : # even
                s = s*10 + even.pop()
            else :
                s = s*10 + odd.pop()
        return s