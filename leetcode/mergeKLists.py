import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return lists
        q = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(q,(lists[i].val,i))
        if not q :
            return None
        # print(q)
        (v,i) = heapq.heappop(q)
        ans = lists[i]
        lists[i] = lists[i].next
        if lists[i]:
            heapq.heappush(q,(lists[i].val,i))
        prevList = ans
        ans.next = None
        while q:
            # print(q,ans)
            (v,i) = heapq.heappop(q)
            # print("1prevList:",prevList)
            prevList.next = lists[i]
            prevList = lists[i]
            lists[i] = lists[i].next
            prevList.next = None
            # print("2prevList:",prevList)
            # print(v,i,lists[i])
            if lists[i]:
                heapq.heappush(q,(lists[i].val,i))
            if prevList:
                prevList.next = None
        prevList.next = None
        return ans