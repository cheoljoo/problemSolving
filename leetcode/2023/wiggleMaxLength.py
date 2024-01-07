class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        old = nums[0]
        count = 1
        isPositive = -1
        for i in range(1,len(nums)):
            v = nums[i]
            if old == v:
                continue
            if isPositive == -1:
                if v > old:
                    isPositive = 1
                else :
                    isPositive = 0
                count += 1
            else:
                if v > old and isPositive == 0:
                    isPositive = 1
                    count += 1
                elif v < old and isPositive == 1:
                    isPositive = 0
                    count += 1
            old = v
        return count
                
# [1,7,4,9,2,5]   , 6
# [1] , 1
# [1,17,5,10,13,15,10,5,16,8] , 7
# [1,2,3,4,5,6,7,8,9] , 2
# [1,2,3,4,5,6,7,8,9,9,9] , 2
# [1,1,1,1,1] , 1
# [10,9,8,7,6] , 2
