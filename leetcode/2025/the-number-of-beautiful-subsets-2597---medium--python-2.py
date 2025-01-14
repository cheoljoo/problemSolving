# 9.27%  Runtime: 2596ms
class Solution:
    #  the count is adjusted by subtracting 1 to exclude the empty subset from the result.
    # time; (2^n)
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # freq: hashtable
        def dp(i, freq):
            if i == len(nums):
                return 1
            # not take
            res = dp(i + 1, freq)
            # freq[nums[i] = k] != 0
            if not freq[nums[i] - k] and not freq[nums[i] + k]:
                freq[nums[i]] += 1
                res += dp(i + 1, freq)
                freq[nums[i]] -= 1
            return res
        return dp(0, defaultdict(int)) - 1