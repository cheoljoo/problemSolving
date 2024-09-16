from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        for n in nums:
            d[n] = 0
        while head:
            if head.val in d:
                head = head.next
            else:
                break
        node = head.next
        prev = head
        while node:
            if node.val in d:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next

        return head

if __name__ == "__main__":
    nums = [1,2,3]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    ans = sol.modifiedList(nums, head)
    while ans:
        print(ans.val, end=" ")
        ans = ans.next

