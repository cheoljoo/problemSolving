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

# minOperations.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        lsum = {}
        rsum = {}
        sol = []
        t = 0
        ans = math.inf
        endFlag = True
        sol.append(math.inf)
        # print(nums,x)
        lsum[0] = 0
        for i,v in enumerate(nums):
            t += v
            if t > x:
                endFlag = False
                break
            lsum[t] = i+1
            if t == x:
                endFlag = False
                sol.append(i+1)
        if endFlag == True:
            return -1
        t = 0
        rsum[0] = 0
        for i,v in enumerate(reversed(nums)):
            t += v
            if t > x:
                break
            rsum[t] = i+1
            if t == x:
                sol.append(i+1)
        # print("lsum:",lsum)
        # print("rsum:",rsum)
        for k,v in lsum.items():
            t = x - k
            ans = min(ans,rsum.get(t,math.inf) + v)
        if ans == math.inf:
            return -1
        else :
            return ans
           
def run(s,s1,expect):
    # print(len(s)," ",end="")
    start = time.time()
    A = Solution()
    r = A.minOperations(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='minOperations.py',
        description=
        'minOperations'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('minOperations problem :')

    run([1,1,4,2,3],5,2)
    run([2,2,2,2,1,20,3,6],9,2)
    run([2,2,2,2,1,7,20,3,6],18,7)
    run([5,6,7,8,9],4,-1)
    run([3,2,20,1,1,3],10,5)
    run([5,2,3,1,1],5,1)
    run([6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119],31841,6)
    run([2,2,2,2,1,7,20,3,6],30,-1)
    run([1,1],3,-1)

# 6016 11499 12040 16365 24514 28029 35894
# 9119 16945 19801 20408
