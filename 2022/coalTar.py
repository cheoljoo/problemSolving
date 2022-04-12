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

# coalTar.py : https://github.com/cheoljoo/problemSolving/tree/master/leetcode

timeFlag = 0
debugFlag = 0
import math

class Solution:
    def coalTar(self, nums: List[int]) -> int:
        l = math.inf
        r = -1
        highest = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                l = i-1
                break
        if l == math.inf:
            return 0
        for i in reversed(range(1,len(nums))):
            if nums[i-1] < nums[i]:
                r = i
                break
        if r == -1:
            return 0
        nums = nums[l:r+1]
        fill = []
        h = []
        a = []
        mx = 0
        for i in range(len(nums)):
            fill.append(0)
            h.append([nums[i],i])
            a.append(0)
        h.sort(reverse=True)
        highest = h[0][1]
        sum = 0
        for i in range(1,len(h)):
            if fill[h[i][1]] != 0 :
                continue
            start = min(h[i][1],highest)
            end = max(h[i][1],highest)
            height = min(h[i][0],nums[highest])
            for j in range(start,end+1):
                if height >= fill[j]:
                    fill[j] = max(height,nums[j])
                    sum += height - nums[j]
                    a[j] = height - nums[j]

        return sum 

        # split l .. highest , highest+1 .. r+1
         
           
def run(s,expect):
    print(s,end="")
    start = time.time()
    A = Solution()
    r = A.coalTar(s)
    print(" total_time1 : ", time.time() - start , "-> ", end="") 
    
    if r == expect:
        print("SUCCESS -> ",end="")
    else :
        print("ERROR(",expect,") -> ",sep="",end="")
    print(r , end="")  
    print()

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(
        prog='coalTar.py',
        description=
        'coalTar'
    )
    parser.add_argument( '--debug', '-d' , action='store_const' , const=1 , help='debug on')

    args = parser.parse_args()
    debug = args.debug
    if not debug:
        debug = 0

    print('coalTar problem :')

    run([1,2,3,5,7,9,4,3,5,7,15,14,12,9,5,3,6,5,8,15,9,4,5,8,5,4,2],82)