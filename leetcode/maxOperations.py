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

# maxOperations.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = {}
        for v in nums:
            if v in c:
                c[v] += 1
            else :
                c[v] = 1
        pair = 0
        for v in c.keys():
            count = c[v]
            p = k - v
            if p == v:
                pair += count // 2
                c[v] = 0
            else :
                if p in c:
                    mn = min(c[v],c[p])
                    pair += mn
                    c[v] -= mn
                    c[p] -= mn
        return pair
                
           
def run(s,s1,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.maxOperations(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maxOperations.py',
        description=
        'maxOperations'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maxOperations problem :')

    run([1,2,3,4],5,2)
    run([3,1,3,4,3],6,1)
    run([3,3,4,4,5,9,10,20,11,15,9,9,8,8,10],18,4)
    run([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2],3,4)
