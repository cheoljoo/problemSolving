# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # traverse with sorted order.
        # if this order is not proper , it is mistake for swapping.
        self.order = []
        self.traverse(root)
        
        self.reOrder = sorted(self.order)
        # print(self.order)
        # print(self.reOrder)
        for i in range(len(self.order)):
            a , aroot = self.order[i]
            b , broot = self.reOrder[i]
            if a != b:
                aroot.val , broot.val = broot.val , aroot.val
                break
    def traverse(self,root: Optional[TreeNode]):
        if not root:
            return
        self.traverse(root.left)
        self.order.append([root.val,root])
        # print(root.val)
        self.traverse(root.right)
        