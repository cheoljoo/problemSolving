# 2466. Count Ways To Build Good Strings : Time Limit Exceeded 26 / 36 testcases passed

# 이것은 timeout 이 된다. 그러나, 4360 정도까지는 문제를 해결한다.
# O(N^2) alogrithm으로  10^5 개에 대해서 N^2 이므로 당연 싶패
# pascal의 triangle로 도 풀어봤지만 (level에 해당하는 array를 바로 구할수 있음) ,  min / max level이 대부분이 되므로 매번 array를 만드는 것으로 더 느려짐.
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        ans = 0
        M = 10**9 + 7
        # 1,3일때
        #  1:1 , 3:1
        #  2:1 , 4:2 , 6:1
        #  3:1 , 5:3 , 7:3 , 9:1
        #  4:1 , 6:4 , 8:6 , 10:4 , 12:1
        # mn = min(zero,one)  mx=max(zero,one)
        # level 1부터 시작해서 , high < mn * level  이면 stop
        mn = min(zero,one) 
        mx=max(zero,one)
        ans = 0
        level = high // mn
        diff = mx - mn
        q = [ [mn,1],[mx,1]]
        if low <= mn <= high:
            ans += 1
        if low <= mx <= high:
            ans += 1
        for i in range(1,level):
            f1 , _ = q[0]
            if low <= (f1+mn) <= high:
                ans += 1
            q[0][0] = f1+mn
            prev = 1
            for j in range(len(q)-1):
                n = q[j][0] + diff
                v = prev + q[j+1][1]
                prev = q[j+1][1]
                q[j+1][0] = n
                q[j+1][1] = v
                if low <= n <= high:
                    ans += v
            if low <= (q[-1][0]+diff) <= high:
                ans += 1
            q.append( [q[-1][0]+diff,1] )
            # print('q',q,'ans',ans)
            ans %= M
        return ans
 
 
# copy solution  O(N)
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = int(1e9 + 7)
        dp = [0] * (high + 1)
        # '' 일때는 아무것도 없는 것으로 stringlength가 0 인 것이 1개가 되는 것을 의미한다.
        dp[0] = 1  # Base case: 1 way to create an empty string
 
        for i in range(high + 1):
            if dp[i] > 0:
                if i + zero <= high:
                    # [i]칸에 zero 만큼을 더해준 [i+zero] 에 [i] 칸의 값을 더해준다.  one도 마찬가지다.
                    dp[i + zero] = (dp[i + zero] + dp[i]) % mod
                if i + one <= high:
                    dp[i + one] = (dp[i + one] + dp[i]) % mod
 
        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % mod
        return result