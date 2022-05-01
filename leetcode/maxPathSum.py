# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # print()
        self.ans = -math.inf
        self.tree = defaultdict()
        self.dfs(root,0)
        self.mx = self.tree[root]
        return self.ans
        
    def dfs(self,root,rootSum):
        leftSum ,rightSum = -math.inf , -math.inf
        rootSum += root.val
        if root.left:
            leftSum = self.dfs(root.left,rootSum)
        if root.right:
            rightSum = self.dfs(root.right,rootSum)
        if max(leftSum,rightSum) >= 0:
            t = root.val + max(leftSum,rightSum)
        else :
            t = root.val
        # t = max(t,0)
        
        self.tree[root] = [root.val,leftSum,rightSum,t,0]  # root.val , left,right,maxUntil,upperMax (step2)
        self.value = max(self.tree[root][:3])
        self.value = max(self.value,self.tree[root][1]+root.val,self.tree[root][2]+root.val,self.tree[root][1]+self.tree[root][2]+root.val)
                 
        self.tree[root][4] = self.value
        # print(self.tree[root] )
        self.ans = max(self.ans,self.value)
        return t
            