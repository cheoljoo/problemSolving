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

# mugCup.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def mugCup(self, n: int,s :List[List[int]]) -> int:
        s.sort()
        stack = []
        sm = 0
        for i in range(n-1):
            v = s[i][1]
            vNext = s[i+1][1]
            if v > vNext:
                sm += vNext
                while stack:
                    if stack[-1] > vNext:
                        sm += vNext
                        stack.pop()
                    else :
                        break
            else :
                stack.append(v)
        sm += sum(stack)
        sm += s[n-1][1]
        print(s)        
        return sm

           
def run(s,s1,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.mugCup(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='mugCup.py',
        description=
        'mugCup'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('mugCup problem :')

    run(4,[[2,15],[7,12],[5,46],[9,7]],38)
    run(5,[[1,15],[2,14],[3,13],[4,12],[5,11]],61)
    run(9,[[1,2],[2,4],[3,6],[4,3],[5,1],[6,4],[7,2],[8,10],[9,3]], 1+3+3+1+1+2+2+3+3)