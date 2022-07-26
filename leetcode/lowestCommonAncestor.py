# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.anc = {}
        self.panc = {}
        que = [root]
        matchCount = 0
        while que and matchCount < 2:
            node = que.pop(0)
            if node.left:
                self.anc[node.left] = node
                que.append(node.left)
            if node.right:
                self.anc[node.right] = node
                que.append(node.right)
            if node == p or node == q:
                matchCount += 1
        
        while p: 
            # print("p:",p.val)
            self.panc[p] = 1
            if p == root:
                break
            p = self.anc[p]
            
        while q: 
            # print("q;",q.val)
            if q in self.panc:
                return q
            if q == root:
                break
            q = self.anc[q]
            
        return root
            
                