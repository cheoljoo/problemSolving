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

# firstMissingPositive.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        M = 5*(10**5)+1
        mem = [0 for _ in range(M)]
        mem[0] = 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            if nums[i] >= M:
                continue
            else :
                mem[nums[i]] = 1
        for i in range(M):
            if not mem[i] :
                return i
        return M

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.firstMissingPositive(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='firstMissingPositive.py',
        description=
        'firstMissingPositive'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('firstMissingPositive problem :')

    run([1,2,0],3)
    run([3,4,-1,1],2)
    run([7,8,9,11,12],1)