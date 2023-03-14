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
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        s = 1
        e = totalTrips * time[0] + 1
        cnt = 0
        while s < e:
            mid = (s+e) // 2
            ans = 0
            for v in time:
                ans += mid // v
            # print(s,mid,e,ans,time,totalTrips)
            if ans == totalTrips:
                for i in reversed(range(s,mid)):
                    p = 0
                    for v in time:
                        p += i // v
                    if p != ans:
                        return i+1
                return mid
            p = 0
            for v in time:
                p += (mid -1) // v
            if p < totalTrips and ans >= totalTrips:
                return mid
            if ans > totalTrips:
                e = mid
            else :
                s = mid
            cnt += 1
        return -1