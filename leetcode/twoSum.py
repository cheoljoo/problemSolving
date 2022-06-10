class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startIdx = 0
        endIdx = 1
        # print(numbers,target)
        while startIdx < endIdx:
            # print(startIdx,endIdx)
            sm = numbers[startIdx] + numbers[endIdx]
            if sm == target:
                return [startIdx+1,endIdx+1]
            elif sm < target:
                if endIdx +1 == len(numbers):
                    startIdx += 1
                elif numbers[startIdx] + numbers[endIdx+1] <= target:
                    endIdx += 1
                else:
                    # print("bigger",startIdx,endIdx+1,numbers[startIdx],numbers[endIdx],numbers[endIdx+1],":",numbers[startIdx] + numbers[endIdx+1] ,">",target)
                    startIdx += 1
            else :
                # print("error",startIdx,endIdx,numbers[startIdx],numbers[endIdx])
                endIdx -= 1
        return []

# [2,7,11,15]
# 9
# [2,3,7,11,15]
# 14
# [2,3,4]
# 6
# [-1,0]
# -1
# [1,3,5,7,9,10,12,14,16,30]
# 22
# [1,3,5,7,9,10,12,14,16,30]
# 25
# [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
# 542
