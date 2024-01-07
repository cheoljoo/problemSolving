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

# largestRectangleArea.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        data = []
        count = 1
        for i in range(1,len(heights)):
            if heights[i-1] == heights[i]:
                count += 1
            else :
                data.append([heights[i-1],count])
                count = 1
        data.append([heights[-1],count])

        mx = 0
        for i in range(len(data)):
            v = data[i][0]
            c = data[i][1]
            count = c
            for j1 in reversed(range(i)):
                if data[j1][0] >= v:
                    count += data[j1][1]
                else :
                    break
            for j1 in range(i+1,len(data)):
                if data[j1][0] >= v:
                    count += data[j1][1]
                else :
                    break
            mx = max(mx,v*count)
        #print(data)
        return mx

           
def run(s,expect):
    print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.largestRectangleArea(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='largestRectangleArea.py',
        description=
        'largestRectangleArea'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('largestRectangleArea problem :')

    run([2,1,2],3)
    run([2,1,5,6,2,3],10)
    run([2,4],4)