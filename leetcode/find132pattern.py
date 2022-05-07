from collections import defaultdict
from collections import Counter
import collections
import enum
# from re import A
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

timeFlag = 0
debugFlag = 0
import math

# find132pattern.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        idx = 0
        while idx != len(nums)-1:
            if nums[idx] == nums[idx+1]:
                nums.pop(idx)
            else:
                idx += 1
        old , idx = math.inf , 0
        while idx < len(nums):
            if old < nums[idx]:
                break
            old = nums[idx]
            idx += 1
        if idx != 0 :
            idx -= 1
        nums = nums[idx:]
        # old , idx = math.inf , len(nums)-1
        # while idx >=0 :
        #     if old < nums[idx]:
        #         break
        #     old = nums[idx]
        #     idx -= 1
        # if idx != len(nums)-1 :
        #     idx += 1
        # nums = nums[:idx+1]
        if len(nums) < 3:
            return False

        left = [math.inf for _ in range(len(nums))]
        right = [-math.inf for _ in range(len(nums))]
        mn = math.inf
        for i in range(len(nums)):
            left[i] = mn
            mn = min(mn,nums[i])
        # stack = []
        for i in reversed(range(len(nums))):
            mx = -math.inf
            for j in reversed(range(i,len(nums))):
                if nums[i] > nums[j]:
                    mx = max(mx,nums[j])
            right[i] = mx
        # i = 1
        for i in range(len(nums)):
            if left[i] < nums[i] and left[i] < right[i] and nums[i] > right[i]:
                return True
        return False

           
def run(s,expect):
    print(len(s),end="")
    start = time.time()
    A = Solution()
    r = A.find132pattern(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r, s , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='find132pattern.py',
        description=
        'find132pattern'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('find132pattern problem :')

    run([3,5,0,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],True)
    run([3,5,0,2,4,3],True)
    run([1,3,2,4,5,6,7,8,9,10],True)
    run([9,8,7,6,5,3,4,2,1,0,100,7],True)
    run([9,8,100,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],False)
    run([9,8,7,6,5,3,4,2,1,0],False)
    run([1,2,3,4],False)
    run([3,1,4,2],True)
    run([-1,3,2,0],True)
    run([3,3,1,4,4,2],True)
    run([0,0,0],False)
    run([0],False)
    run([1,2],False)