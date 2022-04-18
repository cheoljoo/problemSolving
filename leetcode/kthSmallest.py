# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -1
        self.k = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return -1
        if self.k == -1:
            self.k = k
        self.kthSmallest(root.left,k)
        if self.k == 1 and self.ans == -1 :
            self.ans = root.val
            # print(root.val)
            return self.ans
        self.k -= 1
        self.kthSmallest(root.right,k)
        return self.ans