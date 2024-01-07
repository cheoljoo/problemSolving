  

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for v in nums:
            if v in c:
                c[v] += 1
            else :
                c[v] = 1
        kfreq = []
        for key in c.keys():
            kfreq.append([c[key],key])
        kfreq.sort(reverse=True)
        ans = [key for (i,(value,key)) in enumerate(kfreq) if i < k ]
        return ans