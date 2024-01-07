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

# findTargetSumWays.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans = 0 
        self.mem = {}
        self.count = 0
        t = self.go(0,0,nums,target)
        print(self.count)
        return t
    def go(self,s,n,nums,target):
        if (s,n) in self.mem:
            return self.mem[(s,n)]
        cho = 0
        self.count += 1
        if n == len(nums)-1:
            if s + nums[n] == target:
                cho += 1
            if s - nums[n] == target:
                cho += 1
            self.mem[(s,n)] = cho
            return cho
        a = self.go(s+nums[n],n+1,nums,target)
        self.mem[(s+nums[n],n+1)] = a
        b = self.go(s-nums[n],n+1,nums,target)
        self.mem[(s-nums[n],n+1)] = b
        return a + b

           
def run(s,s1,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.findTargetSumWays(s,s1)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='findTargetSumWays.py',
        description=
        'findTargetSumWays'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('findTargetSumWays problem :')

    run([1,2,1],0,2)
    run([1,1,1,1,1],3,5)
    run([1],1,1)
    run([1,1,1,1],5,0)
    run([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],14,1140)
    run([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,1],200,0)