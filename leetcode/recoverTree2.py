# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.old = -math.inf
        self.a = math.inf
        self.b = math.inf
        self.changeCount = 0
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # traverse twice
        # 1. get list  and check what is mistake
        # 2. change value
        self.traverse(root)
        # print(self.a,self.b)
        self.setTraverse(root,self.a,self.b)
        
    def traverse(self,root: Optional[TreeNode]):
        if not root:
            return
        self.traverse(root.left)
        # print(root.val)
        if self.old < root.val:
            self.old = root.val
        else :
            if self.a == math.inf:
                self.a = self.old
            self.b = root.val
        self.traverse(root.right)
    def setTraverse(self,root: Optional[TreeNode],a , b):
        if not root:
            return
        self.setTraverse(root.left,a,b)
        if root.val == a:
            root.val = b
            self.changeCount += 1
        elif root.val == b:
            root.val = a
            self.changeCount += 1
        if self.changeCount == 2 :
            return
        self.setTraverse(root.right,a,b)
        