# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        ans = []
        while q:
            sm = 0
            cnt = 0
            nextq = []
            while q:
                node = q.pop(0)
                sm += node.val
                cnt += 1
                if node.left:
                    nextq.append(node.left)
                if node.right:
                    nextq.append(node.right)
            if cnt != 0:
                ans.append(sm/cnt)
            q = nextq
        return ans
            