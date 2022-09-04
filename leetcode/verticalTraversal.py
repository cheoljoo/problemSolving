# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [(root,0,0)]
        ans = {}  # { [] }
        l = set()
        while q:
            node , lvl , order = q.pop(0)  # sorted by order , lvl , val
            l.add(order)
            if order not in ans:
                ans[order] = []
            ans[order].append((lvl,node.val))
            if node.left:
                q.append((node.left,lvl+1,order-1))
            if node.right:
                q.append((node.right,lvl+1,order+1))
            # print("ans:",ans)
        srt = list(l)
        srt.sort()
        tt = []
        for order in srt:
            p = ans[order]
            p.sort()
            t2 = []
            for lvl,val in p:
                t2.append(val)
            tt.append(t2)
        # tt = []
        # for k in srt:
        #     p = ans[k]
        #     # p.sort()
        #     tt.append(p)
        # print("tt:====",tt)
        return tt