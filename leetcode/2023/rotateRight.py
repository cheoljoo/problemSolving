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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        size = 0
        node = []
        if (not head) or (not head.next):
            return head
        while cur :
            node.append(cur)
            size += 1
            cur = cur.next
        
        rotate = k % size
        
        if rotate > 0:
            node[size-rotate-1].next = None
            node[size-1].next = head 
            head = node[size - rotate]   # size-1  - (rotate-1)
            
        return head