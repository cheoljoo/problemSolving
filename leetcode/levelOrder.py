"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            next = []
            subAns = []
            while q:
                node = q.pop(0)
                if node :
                    subAns.append(node.val)
                    for child in node.children:
                        next.append(child)
            ans.append(subAns)
            q = next
        return ans