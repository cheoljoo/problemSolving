class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # hash = [0 for _ in range(2**k)]
        d = set()
        # st = [0 for _ in range(k)]
        # for i in range(2**k):
        # count = 0
        for i in range(len(s)-k+1):
            # count += 1
            d.add(s[i:i+k])
        # print(count)
        if len(d) == 2**k :
            return True
        return False

# "00110110"
# 2
# "0110"
# 1
# "0110"
# 2
# "1"
# 1
# "00110"
# 2