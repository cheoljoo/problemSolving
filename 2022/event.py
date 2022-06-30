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

# event.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def event(self, M: int,order:List[List[int]]) -> List[int]:
        N = len(order)
        ans = [0 for _ in range(N)]
        for i in range(N):
            e = [0 for _ in range(M)]
            eCount = 0
            for j in range(i,N):
                a1 ,a2 = order[j]
                a1 -= 1
                a2 -= 1
                if e[a1] == 0:
                    eCount += 1
                    e[a1] = 1
                elif e[a2] == 0:
                    eCount += 1
                    e[a2] = 1
                if eCount >= M:
                    ans[i] = eCount
                    break
            ans[i] = eCount
        return ans

           
def run(s,s1,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.event(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='event.py',
        description=
        'event'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('event problem :')

    run(2,[[1,2],[2,1],[2,1],[1,2]],[2,2,2,1])

