import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.heapq = nums[:k]
        # print(nums,k)
        heapq.heapify(self.heapq)
        # print(self.heapq)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heapq) < self.k:
            heapq.heappush(self.heapq,val)
            return self.heapq[0]
        if val <= self.heapq[0] : 
            return self.heapq[0]
        else :
            heapq.heappop(self.heapq)
            heapq.heappush(self.heapq,val)
            return self.heapq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
# ["KthLargest","add","add","add","add","add"]
# [[1,[]],[-3],[-2],[-4],[0],[4]]
# ["KthLargest","add","add","add","add","add"]
# [[2,[0]],[-1],[1],[-2],[-4],[3]]  