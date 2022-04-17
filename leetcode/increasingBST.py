# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root = None
        self.cur = None
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        # traverse
        self.increasingBST(root.left)
        if self.root == None:
            self.root = root
            self.cur = root
        else :
            self.cur.left = None
            self.cur.right = root
            self.cur = root
        # print(root.val)
        self.increasingBST(root.right)
        #specific test case : need to finialize
        self.cur.left = None
        self.cur.right = None
        return self.root