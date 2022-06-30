class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        self.mem = {}
        avg = sum(nums) // len(nums)
        mx = max(nums)
        mn = min(nums)
        while avg >= mn and avg <= mx and mn <= mx:
            a = self.getCnt(avg,nums)
            b = self.getCnt(avg-1,nums)
            # print(mx,"avg:",avg,"a,b:",a,b)
            if b < a :
                mx = avg
                avg = (avg + mn) // 2
                continue
            c = self.getCnt(avg+1,nums)
            # print(mx,"avg:",avg,"a,c:",a,c)
            if c < a :
                mn = avg
                avg = (avg + mx) // 2
                continue
            return a

     

    def getCnt(self,avg,nums):
        if avg in self.mem:
            return self.mem[avg]
        cnt = 0
        for i in nums:
            cnt += abs(avg - i)
        self.mem[avg] = cnt
        return cnt