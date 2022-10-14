class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums):
            if nums[0] == 0:
                nums.pop(0)
            else:
                break
        index = {}
        ans = 0
        if len(nums) < 3:
            return 0
        for i,v in enumerate(nums):
            index[v] = i
        for i in range(nums[0],nums[-1] + 1):
            if i not in index:
                index[i] = index[i-1]
        # print("index:",index)
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                end = nums[i]+ nums[j] - 1
                if end > nums[-1] or end < 0:
                    fi = index[nums[-1]]
                else:
                    fi = index[end]
                # print(i,j,end,fi)
                ans += fi-j
        return ans
