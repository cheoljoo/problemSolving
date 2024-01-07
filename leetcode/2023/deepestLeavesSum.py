# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.maxDepth = 0
        self.dfs(root,1)
        return self.ans
    def dfs(self, root: Optional[TreeNode],depth:int):
        if root.left == None and root.right == None:   # leaf node
            if self.maxDepth < depth:
                self.maxDepth = depth
                self.ans = root.val
            elif self.maxDepth == depth:
                self.ans += root.val
            return
        if root.left:
            self.dfs(root.left,depth+1)
        if root.right:
            self.dfs(root.right,depth+1)
        
        