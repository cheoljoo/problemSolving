from collections import defaultdict
from re import A
#import numpy as np

import sys
import argparse
import math
import random
# https://www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.stack = []
        self.result = True
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.getHeight(root)
        return self.result
    
    def getHeight(self,root:Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if abs(leftHeight - rightHeight) > 1:
            self.result = False
        return max(leftHeight,rightHeight) + 1
    
    def makeTree(self, s:List[Optional[int]]) -> Optional[TreeNode]:
        if len(s) == 0:
            return None
        height = 1
        lvlSum = 1
        head = TreeNode(s[0])
        self.stack.append(head)
        for i in range(1,len(s)):
            if i >= lvlSum:
                lvlSum += 2**height
                height += 1
            
            if s[i] :  # not None
                node = TreeNode(s[i])
                self.stack.append(node)
                if i%2 == 1:
                    parent = self.stack.pop(0)
                    parent.left = node
                else :
                    parent.right = node
            else :
                if i%2 == 1:
                    parent = self.stack.pop(0)
                    
        return head

def run(s,expect):
    A = Solution()
    head = A.makeTree(s)
    r = A.isBalanced(head)
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='isBalanced.py',
        description=
        'isBalanced'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    s = [3,9,20,None,None,15,7]
    run(s,True)
    s = [1,2,3,4,5,None,None,6,7]
    run(s,False)
    s = []
    run(s,True)
