class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.f = {} # this is final result.
        nums.sort()
        ans = 0
        # print(nums)
        for i,v in enumerate(nums):
            if v > target:
                break
            self.goWithTarget(nums[:i+1],v)
        print("main f:",self.f)
        if target in self.f:
            return self.f[target]
        else:
            for i,v in enumerate(nums):
                if (target - v) in self.f:
                    ans += self.f[target-v]
            return ans
    def goWithTarget(self, nums: List[int], target: int) -> int:
        r = 1
        for i in range(len(nums)-1):
            # print("f:",self.f,target,i,nums)
            if (target - nums[i]) in self.f:
                r += self.f[(target - nums[i])]
                # print(r)
        self.f[target] = r
        print("r f:",self.f,target,nums)
        return r
            
    