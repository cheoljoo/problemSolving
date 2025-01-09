# 2471. Minimum Number of Operations to Sort a Binary Tree by Level : Runtime 286ms Beats 20.38%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        level = defaultdict(list)
        level_hq = defaultdict(list)
        level_idx = defaultdict(dict)
 
        # dfs 를 진행 하며 같은 레벨의 값들을 분류
        def dfs(node, lev):
            heapq.heappush(level_hq[lev], node.val)
            level_idx[lev][node.val] = len(level[lev]) # value : index
            level[lev].append(node.val)
 
            if node.left:
                dfs(node.left, lev + 1)
            if node.right:
                dfs(node.right, lev + 1)
 
        dfs(root, 0)
        cnt = 0
 
        for k, v in level.items():
            for i in range(len(v)):
                value = heapq.heappop(level_hq[k])
 
                if v[i] > value:
                    idx = level_idx[k][value]
                    v[i], v[idx] = v[idx], v[i] # value swap
                    level_idx[k][v[i]], level_idx[k][v[idx]] = i, idx # index swap
                    cnt += 1
 
        return cnt