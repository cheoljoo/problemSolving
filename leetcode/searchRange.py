class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        ans = []
        a = bisect_left(nums,target)
        if  a < len(nums) and nums[a] == target:
            ans.append(a)
        else :
            ans.append(-1)
        b = bisect_right(nums,target)
        if b-1 < len(nums) and nums[b-1] == target:
            ans.append(b-1)
        else :
            ans.append(-1)
        return ans