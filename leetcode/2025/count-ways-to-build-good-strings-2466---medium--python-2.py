# 2466. Count Ways To Build Good Strings : Runtime 95ms Beats 62.29%

'''
# Memory Limit Exceeded 32/36 testcases passed
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        memo = [-1] * (high + 1)
 
        def dp(len_str):
            if len_str > high:
                return 0
            if memo[len_str] >= 0:
                return memo[len_str]
 
            cnt = 0
            if low <= len_str <= high:
                cnt += 1
 
            cnt += dp(len_str + zero)
            cnt += dp(len_str + one)
 
            memo[len_str] = cnt
 
            return cnt
         
        return dp(0) % (10 ** 9 + 7)
 
# Runtime 1016 ms Beats 6.03% Memory 680.02MB Beats 5.28%
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        memo = [0] * (high + 1)
        memo[zero] += 1
        memo[one] += 1
 
        for n in range(min(one, zero), high + 1):
            if n - zero > 0:
                memo[n] += memo[n - zero]
            if n - one > 0:
                memo[n] += memo[n - one]
 
        return sum(memo[low:high + 1]) % (10 ** 9 + 7)
'''
# Runtime 95ms Beats 62.29% Memory 22.10MB Beats 75.11%
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        memo = [0] * (high + 1)
        memo[zero] += 1
        memo[one] += 1
 
        for n in range(min(one, zero), high + 1):
            if n - zero > 0:
                memo[n] += memo[n - zero]
            if n - one > 0:
                memo[n] += memo[n - one]
            memo[n] %= (10 ** 9 + 7) # 이 한 줄 추가로 실행 속도, 메모리 사용량 대폭 감소
 
        return sum(memo[low:high + 1]) % (10 ** 9 + 7)