# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        # print("root:",root.val)
        self.end = root
        right = root.right
        if root.left:
            self.traverse(root.left)
        if right:
            self.traverse(right)
    def traverse(self,child):
        # print("child:",child.val)
        right = child.right
        self.end.left = None
        self.end.right = child
        self.end = child
        if child.left:
            self.traverse(child.left)
        if right:
            self.traverse(right)
        return