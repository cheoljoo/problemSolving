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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = []
        self.visit(root,0)
        # print(self.ans)
        return sum(self.ans)
    def visit(self,root,Sum):
        # print(root.val,Sum)
        if not root.left and not root.right:
            self.ans.append(root.val + Sum)
            return
        Sum += root.val
        if root.left:
            self.visit(root.left,Sum*10)
        if root.right:   
            self.visit(root.right,Sum*10)
        return