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

# countBits.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        s = 1
        e = piles[-1]
        minv = e
        while s < e:
            k = (s+e) // 2
            # print(s,k,e)
            ans = 0
            for p in piles:
                if p % k == 0:
                    ans += p // k
                else :
                    ans += p // k  + 1
            if ans <= h:
                minv = min(minv,k)
                e = k
            elif ans > h:
                s = k + 1
        return minv
    
'''
[3,6,7,11]
8
[30,11,23,4,20]
5
[30,11,23,4,20]
6
[5,5]
100
[5,6,7]
13
[1,100,5,43]
13000
'''