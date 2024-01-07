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

# nextPermutation.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        for i in reversed(range(1,len(nums))):
            if i == 0 :
                break
            if nums[i-1] < nums[i]:
                break
        if i == 0:
            nums.sort()
            return nums
        findNextMin = math.inf
        findNextIndex = -1
        cur = nums[i-1]
        for k in range(i,len(nums)):
            if cur < nums[k]:
                if findNextMin > nums[k] :
                    findNextMin = nums[k]
                    findNextIndex = k
        nums[i-1] , nums[findNextIndex] = nums[findNextIndex] , nums[i-1]
        
        nums[i:] = sorted(nums[i:])   # in place sort
        # t = nums[i:]
        # t.sort()
        # nums = nums[:i] + t
        return nums
                    
           
def run(s,expect):
    start = time.time()
    A = Solution()
    r = A.nextPermutation(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='nextPermutation.py',
        description=
        'nextPermutation'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('nextPermutation problem :')

    run([1,3,2],[2,1,3])
    run([1,2,3],[1,3,2])
    run([3,2,1],[1,2,3])
    run([1,1,5],[1,5,1])
    run([1,3,7,5,4],[1,4,3,5,7])
    run([1,4,7,5,3],[1,5,3,4,7])
    run([1],[1])