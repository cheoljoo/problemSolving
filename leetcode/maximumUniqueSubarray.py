class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sm = 0
        mem = set()
        sumMem = 0
        pos = {}
        start = 0
        # print("nums:",nums)
        for i,v in enumerate(nums):
            if v not in mem:
                mem.add(v)
                sumMem += v
                pos[v] = i
            else :
                # print("i:",i,"v:",v,"sm:",sm,"sum(mem):",sum(mem),"start:",start,"pos[v]:",pos[v],mem,end=" ")
                # sm = max(sm , sum(mem))
                sm = max(sm,sumMem)
                while start < pos[v]:
                    mem.remove(nums[start])
                    sumMem -= nums[start]
                    start += 1
                
                start = pos[v] + 1
                pos[v] = i
                # print(nums[start:i+1])
        # sm = max(sm , sum(mem))    
        sm = max(sm,sumMem)
        return sm