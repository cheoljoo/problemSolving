# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        if root.right:
            self.convertBST(root.right)
        print(root.val)
        root.val += self.sum
        self.sum = root.val
        if root.left:
            self.convertBST(root.left)        
        return root

# 아래 코드는 무의미함. 
# 왜 아래와 같이 복잡하게 생각했을까?
# 결국은 traverse한 순서로 도하면 되는 것을 알았는데 , left, right 에 따라 다르게 처리할게 아닌 return할때의 순서만 지키면 되는데!!!!        
        if root.right:
            self.convertBST(root.right)
            root.val += self.sum
        self.sum += root.val
        if root.left:
            self.convertBST(root.left)
            root.val += self.sum
        return root
    def goBST(self,root: Optional[TreeNode],child: Optional[TreeNode]):
        # if child == None:
        #     return None
        print(">",self.right,child.val)
        if child.right:
            self.goBST(child,child.right)
            child.val += self.right
            print("R:",self.right,child.val,child.right.val)
            self.right = child.val
        print("S:",self.right)
        if child.left:
            self.goBST(child,child.left)
            child.left.val += self.right
            print("L:",self.right,child.val,child.left.val)
        print("<",self.right,child.val)