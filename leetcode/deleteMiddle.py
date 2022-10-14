# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        doubleNode = head
        node = head
        flagOdd = True
        if node.next == None:
            return None
        doubleNode = doubleNode.next
        while doubleNode:
            oldNode = node
            
            if doubleNode.next:
                doubleNode = doubleNode.next.next
                flagOdd = True
            else:
                doubleNode = doubleNode.next
                flagOdd = False
                break
            node = node.next
        # print(node.val,oldNode.val,flagOdd)
        # if flagOdd == False:
        if oldNode.next:
            oldNode.next = oldNode.next.next
        return head
