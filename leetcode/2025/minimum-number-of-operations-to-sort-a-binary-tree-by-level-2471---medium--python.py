# 2471. Minimum Number of Operations to Sort a Binary Tree by Level : Runtime 293 ms Beats 14.41%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        self.d = {}
        self.dfs(root.left,1)
        self.dfs(root.right,1)
        # print(self.d)
        cnt = 0
        for level,l in self.d.items():
            cnt += self.sort(l)
                # 7,6,4,5 -> 4,6,7,5 -> 4,5,7,6 -> 4,5,6,7
                # 7,6,4,5 -> 7,6,5,4 -> 2번
        # print(self.d)
        return cnt
    def sort(self,l):
        cnt = 0
        sorto = [ [i,l[i]] for i in range(len(l))]
        sortloidx = defaultdict(int)
        sortl = sorted(sorto,key = lambda x : x[1])
        # print('sorto',sorto)
        # print('sortl',sortl)
        for i in range(len(sorto)):
            sortloidx[sorto[i][0]] = i
        # print('sortloidx',sortloidx)
        for ii in range(len(sortl)):
            ## if sortl[ii] == ii 이면 딱 맞는자리로 swap필요없음
            # print('ii',ii,'l',sortl,'o',sorto,cnt)
            if sortl[ii][0] != sorto[ii][0]:
                lx = sortl[ii][0]
                ox = sorto[ii][0]
                a = sortloidx[lx]
                b = sortloidx[ox]
                # print('1a',a,'b',b,'sortloidx',sortloidx,sorto)
                sorto[a] , sorto[b] = sorto[b] , sorto[a]
                # print('2a',a,'b',b,'sortloidx',sortloidx,sorto)
                sortloidx[lx] = b
                sortloidx[ox] = a
                ##wrong# tt = sortloidx[ii]
                ##wrong# sortloidx[ii] = sortloidx[sortl[ii][0]]
                ##wrong# sortloidx[sortl[ii][0]] = tt
                ##wrong# sortloidx[sortl[ii][0]] , sortloidx[sorto[ii][0]] = sortloidx[sorto[ii][0]] , sortloidx[sortl[ii][0]]
                cnt += 1
                # print('3a',a,'b',b,'sortloidx',sortloidx,'o',sorto,cnt)
            # print('-sorto',sorto , cnt)
        return cnt
             
 
    def dfs(self,node,level):
        if not node:
            return
        if level not in self.d:
            self.d[level] = []
        self.d[level].append(node.val)
        self.dfs(node.left,level+1)
        self.dfs(node.right,level+1)