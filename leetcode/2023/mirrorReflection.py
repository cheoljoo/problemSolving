class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p == 1:
            return 1
        for c in range(1,p+2):
            # c is count
            h = q * c
            # print(h,q,c,p)
            if c % 2 == 0 :
                # c is even && h % 2p == p
                if h % (2*p) == p :
                    return 2
            else :
                if h % (2*p) == p :
                    return 1
                elif h % (2*p) == 0 :
                    return 0
        return -1