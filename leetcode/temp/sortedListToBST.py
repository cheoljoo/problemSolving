from collections import defaultdict
from collections import Counter
from collections import deque
import collections
import enum
from re import A
#import numpy as np

import sys
import argparse
import math
import random
from tkinter import N
# https://www.daleseo.com/python-typing/
from typing import Optional
from typing import Union
from typing import List
from typing import Final
from typing import Dict
from typing import Tuple
from typing import Set

import time
import heapq
from bisect import bisect_left , bisect_right

timeFlag = 0
debugFlag = 0
import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        center = len(nodes) // 2
        tn = TreeNode(nodes[center])
        leftNodes = nodes[ :center]
        rightNodes = nodes[center +1:]
        self.makeTree(tn,leftNodes,rightNodes)
        return tn
    def makeTree(self,tn,ln,rn):
        if ln:
            c = len(ln) // 2
            tl = TreeNode(ln[c])
            tn.left = tl
            self.makeTree(tl,ln[:c],ln[c+1:])
        if rn:
            c = len(rn) // 2
            tr = TreeNode(rn[c])
            tn.right = tr
            self.makeTree(tr,rn[:c],rn[c+1:])
        return
        
        