class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        mn = 1
        for i in range(1,n):
            mn *= 10
        mx = mn*10-1
        for i in range(1,10):
            if i+k < 10:
                ans.append(i)
            elif i-k >= 0:
                ans.append(i)
        digit = 1
        # print("===========")
        # print(ans)
        while True:
            digit += 1
            next= []
            for val in ans:
                re = val % 10
                if re+k < 10:
                    tt = val*10 + re+k
                    next.append(tt)
                if re-k >= 0 and k!=0:
                    tt = val*10 + re-k
                    next.append(tt)
            ans = next
            # print("ans:",ans, "digit:",digit)
            if digit == n:
                break
        return ans
            