# 3011. Find if Array Can Be Sorted : Runtime 13 ms Beats 53.34%
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevCountBit = -1
        prevMax = -1
        mx = -1
        for n in nums:
            cBit = self.countBit(n)
            if prevCountBit != cBit:
                prevMax = mx
                mx = -1
            mx = max(mx,n)  
            # print(n,'cBit',cBit,'mx',mx,'prevMax',prevMax)
            if prevMax > n:
                return False
            prevCountBit = cBit
        return True
    def countBit(self,n):
        cnt = 0
        while n:
            if n%2 == 1:
                cnt += 1
            n //= 2
        return cnt