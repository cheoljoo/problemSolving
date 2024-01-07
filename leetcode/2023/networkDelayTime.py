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

# networkDelayTime.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for v in times:
            if v[0] in graph:
                graph[v[0]].append((v[2],v[1]))
            else :
                graph[v[0]] = [(v[2],v[1])]
        ans = [-1 for _ in range(n+1)]
        ansCount = 0
        q = [(0,k)]
        while q:
            weight,node = heapq.heappop(q)
            if ans[node] != -1:
                continue
            ans[node] = weight
            ansCount += 1
            if ansCount == n :
                return weight
            if node in graph:
                for w2,n2 in graph[node]:
                    heapq.heappush(q,(weight+w2,n2))
        return -1 

           
def run(s,s1,s2,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.networkDelayTime(s,s1,s2)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='networkDelayTime.py',
        description=
        'networkDelayTime'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('networkDelayTime problem :')

    run([[2,1,1],[2,3,1],[3,4,1]],4,2,2)
    run([[1,2,1]],2,1,1)
    run([[1,2,1]],2,2,-1)