# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.odd = {}
        self.oddCount = 0
        self.ans = 0
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if root.val not in self.odd:
            self.odd[root.val] = 0
        self.odd[root.val] += 1
        if self.odd[root.val] %2 == 1:
            self.oddCount += 1
        else :
            self.oddCount -= 1
        # print("enter:",self.odd,self.oddCount,self.ans)
        if root.right == None and root.left == None:
            if self.oddCount <= 1 :
                self.ans += 1
        if root.left:
            self.pseudoPalindromicPaths(root.left)
        if root.right:
            self.pseudoPalindromicPaths(root.right)

        self.odd[root.val] -= 1
        if self.odd[root.val] %2 == 1:
            self.oddCount += 1
        else :
            self.oddCount -= 1
        # print("exit:",self.odd,self.oddCount,self.ans,root.val)
        return self.ans