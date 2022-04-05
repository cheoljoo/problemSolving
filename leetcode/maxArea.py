from collections import defaultdict
from collections import Counter
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

# maxArea.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
        sortedHeight = []
        for i,h in enumerate(height):
            sortedHeight.append([h,i])
        sortedHeight.sort(reverse=True)
        minLoc = sortedHeight[0][1]
        maxLoc = minLoc
        maxArea = 0
        for i in range(1,len(sortedHeight)):
            h,loc = sortedHeight[i]
            area = h * max(abs(maxLoc-loc),abs(minLoc-loc))
            maxArea = max(maxArea,area)
            minLoc = min(minLoc,loc)
            maxLoc= max(maxLoc,loc)
        return maxArea


           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.maxArea(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='maxArea.py',
        description=
        'maxArea'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('maxArea problem :')

    run([1,8,6,2,5,4,8,3,7],49)
    run([1,1],1)
    run([1,2,1],2)