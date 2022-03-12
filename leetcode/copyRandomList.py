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


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        newHead = None
        newPrev = None
        mem = {}
        mem[None] = None
        while cur:
            if not newHead :
                newHead = Node(cur.val)
                curNew = newHead
                newPrev = newHead
            else :
                curNew = Node(cur.val)
                newPrev.next = curNew
                newPrev = curNew
            mem[cur] = curNew
            cur = cur.next
        cur = head
        curNew = newHead
        while cur:
            curNew.random = mem[cur.random]
            curNew = curNew.next
            cur = cur.next
        return newHead