# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # traverse and count left / right longest edges' length
        # the answer is maximum sum of left and right edges' length
        self.t = {}
        self.ans = 0
        t= self.traverse(root)
        # print("val:",root.val,t)
        return self.ans
    def traverse(self,r) -> int:
        rl , rr = 0 ,0 
        if r.left:
            rl = self.traverse(r.left)
        if r.right:
            rr = self.traverse(r.right)
        # print("val:",r.val,rl,rr)
        self.ans = max(self.ans,rl + rr)
        return max(rl,rr) + 1