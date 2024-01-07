# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # node.value = (oldMax + 10^4) * 10^6 + currentValue + 10^4
        ans = 0
        q = [root]
        basic = 10**4
        old = 10**6
        root.val = (-10**4 +basic) * old + (root.val + basic)
        # cnt = 0
        while q:
            node = q.pop(0)
            oldMax = node.val // old - basic
            curVal = (node.val % old) - basic
            # print(cnt , oldMax , curVal)
            # cnt += 1
            if curVal >= oldMax:
                ans += 1
                oldMax = curVal
            if node.left:
                newVal = (oldMax + basic) * old + (node.left.val + basic)
                node.left.val = newVal
                q.append(node.left)
            if node.right:
                newVal = (oldMax + basic) * old + (node.right.val + basic)
                node.right.val = newVal
                q.append(node.right)
        return ans