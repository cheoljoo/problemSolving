# 3011. Find if Array Can Be Sorted : Runtime 2 ms Beats 96.29%
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pre_max = min_c = max_c = 0
        bit_cnt = [0] * len(nums)
        for i, v in enumerate(nums):
            # bit count
            # for 문 돌면서 counting 할 경우 23ms Beats 40.65%
            # for n in range(9):
            #     if v & 2 ** n:
            #         bit_cnt[i] += 1
            bit_cnt[i] = v.bit_count()
 
            if 0 < i and bit_cnt[i - 1] == bit_cnt[i]:
                min_c = min(min_c, nums[i])
                max_c = max(max_c, nums[i])
            else:
                # new section
                pre_max = max_c
                min_c = max_c = nums[i]
 
            if pre_max > min_c:
                return False
 
        return True