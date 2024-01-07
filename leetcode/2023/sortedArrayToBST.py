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
        self.r = []
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        head = self.insert(nums,0,len(nums)//2,len(nums))
        return head

    def insert(self,nums:List[int],start:int,mid:int,end:int) -> Optional[TreeNode]:  # end is not included
        if start == end :
            return None
        if start+1 == end :
            return TreeNode(nums[start])
        node = TreeNode(nums[mid])
        nodeLeft = self.insert(nums,start,(start+mid)//2,mid)
        nodeRight = self.insert(nums,mid+1,(mid+1+end)//2,end)
        node.left = nodeLeft
        node.right = nodeRight
        return node
    
    def levelTraverse(self,nums,node:Optional[TreeNode]):
        height = 0
        l = len(nums)
        while l > 0 :
            l -= 2**height
            height += 1
        
        for i in range(1,height+1):
            self.traverseWithLevel(node,1,i)    
    
    def traverseWithLevel(self,node:Optional[TreeNode],height:int,i:int):    
        if height == i :
            if node :
                self.r.append(node.val)
            else :
                self.r.append(None)
        else :
            if node :
                self.traverseWithLevel(node.left,height+1,i)
                self.traverseWithLevel(node.right,height+1,i)

def run(s,expect):
    A = Solution()
    head = A.sortedArrayToBST(s)
    A.levelTraverse(s,head)
    r = A.r
    # printHead(rHead)
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR -> ",end="")
    print(r , ":" , s )   

if (__name__ == "__main__"):
    # problem : https://leetcode.com/problems/regular-expression-matching/

    debug = 0
    parser = argparse.ArgumentParser(
        prog='set_ax_b.py',
        description=
        'this set hates a b'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    s = [-10,-3,0,5,9]
    run(s,[0, -3, 9, -10, None, 5, None])
    s = [1,3]
    run(s,[3, 1, None])
