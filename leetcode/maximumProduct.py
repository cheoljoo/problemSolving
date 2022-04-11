class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            p = heapq.heappop(nums)
            heapq.heappush(nums, p+1)
        ml = 1
        while nums:
            v = heapq.heappop(nums)
            ml *= v
            ml %= 10**9+7
        return ml %(10**9+7)